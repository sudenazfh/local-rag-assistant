from foundry_local_sdk import Configuration, FoundryLocalManager

MODEL_ALIAS = "qwen2.5-0.5b"

config = Configuration(app_name="rag_assistant")
FoundryLocalManager.initialize(config)
manager = FoundryLocalManager.instance

manager.download_and_register_eps()

model = manager.catalog.get_model(MODEL_ALIAS)
model.download()
model.load()

client = model.get_chat_client()
messages = [
    {"role": "system", "content":"You are a helpful, concise assistant." },
    {"role": "user", "content":"Explain what RAG is in two sentences." },
]

print("Assistant: ", end="", flush=True)
for chunk in client.complete_streaming_chat(messages):
    if chunk.choices:
        piece = chunk.choices[0].delta.content
        if piece: 
            print(piece, end="", flush=True)
print()

model.unload()
