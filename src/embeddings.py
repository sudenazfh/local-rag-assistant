from sentence_transformers import SentenceTransformer
from src.config import EMBED_MODEL

_model = None       # lazy loading 

def _get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBED_MODEL)
    return _model

def embed_text(text: str) -> list[float]:
    return _get_model().encode(text).tolist()

def embed_batch(texts: list[str]) -> list[list[float]]:
    return _get_model().encode(texts).tolist()