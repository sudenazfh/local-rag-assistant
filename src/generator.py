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
    "Answer in 3 sentences or fewer, and cite the source document name. "
    "If the context is empty or does not contain the answer, do not guess — "
    "reply only with: \"I don't have that information.\""
)


def answer_query(question: str) -> str:
    chunks = get_top_chunks(question)
    client = _get_client()

   
    context = "\n\n".join(
        f"[source: {c['source']}]\n{c['content']}" for c in chunks
    )

 
    user_message = f"{context}\n\nQuestion: {question}"

 
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]

   
    answer = ""
    for chunk in client.complete_streaming_chat(messages):
        if chunk.choices:
            piece = chunk.choices[0].delta.content
            if piece:
                answer += piece
    return answer


if __name__ == "__main__":
    print(answer_query("What is cosine similarity?"))
