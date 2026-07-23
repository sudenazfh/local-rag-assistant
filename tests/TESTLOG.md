# 🧪 Functional Test Log

**Model:** `phi-4-mini` · **Runtime:** Foundry Local · **Corpus:** 6 docs

**Verdict key:** ✅ correct · ⚠️ weak / too long / off-intent · ❌ wrong / hallucinated

---

## Summary

| #  | Question                       | Type                 | Verdict |
|----|--------------------------------|----------------------|:-------:|
| 1  | What is RAG?                   | in-docs              | ✅ |
| 2  | What is cosine similarity?     | in-docs              | ✅ |
| 3  | How does chunking work here?   | in-docs              | ⚠️ |
| 4  | What are embeddings?           | in-docs              | ⚠️ |
| 5  | What is Foundry Local?         | in-docs              | ✅ |
| 6  | How do I set up the project?   | in-docs              | ⚠️ |
| 7  | Who won the 2022 World Cup?    | out-of-docs → refuse | ✅ |
| 8  | What is the capital of France? | out-of-docs → refuse | ✅ |
| 9  | (empty input)                  | edge case            | ❌ |
| 10 | Tell me about the thing        | vague                | ⚠️ |

---

## Answers

### 1 · What is RAG? — ✅
> Retrieval-Augmented Generation (RAG) is a technique that enhances a language model's ability to answer questions by providing it with access to external knowledge at the time of questioning. It consists of two main phases: ingestion, where documents are processed and stored as embedding vectors, and retrieval and generation, where relevant document chunks are retrieved to inform the model's response. RAG systems are particularly useful for maintaining accuracy and relevance in answers without the need for constant retraining, as they can immediately incorporate new documents into their knowledge base.

`sources: what_is_rag.txt, project_setup.txt`

### 2 · What is cosine similarity? — ✅
> Cosine similarity is a metric used to measure the angle between two vectors, often used to determine how similar two pieces of text are in terms of their meaning. It is calculated by taking the dot product of the vectors and dividing it by the product of their lengths, resulting in a score between -1 and 1, where 1 indicates identical meaning, 0 indicates no relation, and negative values indicate opposite meanings. This method is particularly useful in search and retrieval systems, as it can effectively compare the direction of vectors regardless of their magnitude, making it suitable for comparing texts of different lengths.

`source: cosine_similarity.txt`

### 3 · How does chunking work here? — ⚠️
> Chunking in this project involves splitting documents into smaller pieces, or chunks, to make them more manageable for language models and embedding models. The text is divided into paragraphs and then glued together greedily until reaching about 800 characters, at which point a new chunk begins. This method aims to keep related sentences together while preventing any single chunk from becoming too large. The chunk size is a balance between providing precise matches and maintaining the context of the embedding. The project uses a local RAG assistant built in Python, with the code organized by responsibility and storing document chunks and their embedding vectors in a single SQLite database file.

`sources: chunking.txt, project_setup.txt`

### 4 · What are embeddings? — ⚠️
> Embeddings are lists of numbers that represent the meaning of a piece of text, produced by models like all-MiniLM-L6-v2 from the sentence-transformers library. They allow similar meanings to have similar numerical representations, enabling search engines to find results by meaning rather than exact keywords. Cosine similarity is used to compare these embeddings, measuring the angle between vectors to determine similarity scores. Foundry Local uses embeddings in its chat step, while the sentence-transformers library handles embedding support separately.

`source: embeddings.txt`

### 5 · What is Foundry Local? — ✅
> Foundry Local is a tool that runs a large language model directly on your own computer, ensuring privacy and offline functionality without cloud dependency or API keys. It is used in a project setup where the model reads context and writes answers, with embeddings handled separately by the sentence-transformers library. The project is a local RAG assistant built in Python, storing document chunks and embedding vectors in an SQLite database, and it uses an OpenAI-compatible interface for model access.

`sources: foundry_local.txt, project_setup.txt`

### 6 · How do I set up the project? — ⚠️
> To set up the project, you need to install Python and the required libraries, including the sentence-transformers library for embeddings. Then, you can run the ingest script to load documents into the SQLite database, and use the retriever to find the best chunks for a question. Finally, you can use Foundry Local to run the large language model locally, and the same code style used for the OpenAI API can be used to access the model. The model is accessed through an OpenAI-compatible interface, and the active model in this project is a small, fast model chosen so it runs smoothly on a laptop without freezing the machine.

`sources: project_setup.txt, foundry_local.txt`

### 7 · Who won the 2022 World Cup? — ✅
> I don't have that information.

`out-of-docs → refused correctly`

### 8 · What is the capital of France? — ✅
> I don't have that information.

`out-of-docs → refused correctly`

### 9 · (empty input) — ❌
> Retrieval-Augmented Generation (RAG) is a technique that enhances a language model's responses by providing access to external knowledge at the time of questioning, rather than relying solely on what the model has learned during training. RAG operates in two phases: ingestion, where documents are processed and stored as embedding vectors, and retrieval and generation, where the model uses these stored vectors to find relevant information and generate accurate answers. The main advantage of RAG is that it allows for up-to-date answers without the need for retraining the model, as new documents can be added and utilized immediately after ingestion.

`empty query still retrieved + generated a confident answer → should refuse or prompt`

### 10 · Tell me about the thing — ⚠️
> Retrieval-Augmented Generation (RAG) is a technique that enhances a language model's capabilities by providing it with access to external knowledge at the time of answering a question. It consists of two phases: ingestion, where documents are processed and stored as embedding vectors, and retrieval and generation, where the model uses these stored vectors to find relevant information and generate accurate, up-to-date answers. RAG allows for immediate updates to the system's knowledge base by adding new documents, making it ideal for handling private or frequently changing information without the need for retraining the model.

`sources: foundry_local.txt, what_is_rag.txt`
