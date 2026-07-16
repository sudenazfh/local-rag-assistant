from foundry_local_sdk import FoundryLocalManager
from openai import OpenAI

MODEL_ALIAS = "phi-4-mini"

manager = FoundryLocalManager(MODEL_ALIAS)

client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info(MODEL_ALIAS).id,
    messages=[
        {"role": "system", "content": "You are a helpful, concise assistant."},
        {"role": "user", "content": "Explain what RAG is in two sentences."},
    ],
)

print(response.choices[0].message.content)