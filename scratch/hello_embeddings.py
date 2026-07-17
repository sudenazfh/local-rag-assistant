from sentence_transformers import SentenceTransformer
import numpy as np 

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "The cat sat on the mat.",              # vectors[0]
    "A feline rested on the rug.",          # vectors[1]
    "Python is a programing language.",     # vectors[2]
]

vectors = model.encode(sentences)
print("Vector Shape: ", vectors.shape)

def cosine_similarity(a, b):
    
    similarity_score = np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return similarity_score

print(f"cat vs feline : {cosine_similarity(vectors[0], vectors[1]):.4f}")
print(f"cat vs python : {cosine_similarity(vectors[0], vectors[2]):.4f}")