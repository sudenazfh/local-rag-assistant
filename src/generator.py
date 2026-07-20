# src/generator.py
"""Logic layer: turn a question + retrieved context into a grounded answer."""
from foundry_local_sdk import Configuration, FoundryLocalManager
from src.config import LLM_ALIAS
from src.retriever import get_top_chunks

_client = None


def _get_client():
    global _client
    if _client is None:
        config = Configuration(app_name="rag_assistant")
        FoundryLocalManager.initialize(config)
        manager = FoundryLocalManager.instance
        manager.download_and_register_eps()
        model = manager.catalog.get_model(LLM_ALIAS)
        model.download()
        model.load()
        _client = model.get_chat_client()   # loaded once, reused every call
    return _client


SYSTEM_PROMPT = (
    "You are a helpful assistant that answers ONLY using the provided context. "
    "If the answer is not in the context, say: \"I don't have that information.\" "
    "Cite the source document name in your answer."
)


def answer_query(question: str) -> str:
    chunks = get_top_chunks(question)
    client = _get_client()

    # 1. join each chunk's source + content into one context block
    context = "\n\n".join(
        f"[source: {c['source']}]\n{c['content']}" for c in chunks
    )

    # 2. user message = the context, then the question
    user_message = f"{context}\n\nQuestion: {question}"

    # 3. messages: standing instructions + this turn's message
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

    # 4. stream the reply, accumulate the pieces into one string
    answer = ""
    for chunk in client.complete_streaming_chat(messages):
        if chunk.choices:
            piece = chunk.choices[0].delta.content
            if piece:
                answer += piece
    return answer


if __name__ == "__main__":
    print(answer_query("What is cosine similarity?"))
