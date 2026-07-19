from src.config import CHUNK_MAX_CHARS

def chunk_text(text: str) -> list[str]:
    # ponytail: naive char-based paragraph chunking. Upgrade to token-aware or
    # sentence-boundary splitting only if answer quality suffers.
    pharagraphs = text.split("\n\n")
    chunks = []
    current = ""
    for para in pharagraphs:
        para = para.strip()
        if not para:
            continue
        if current and len(current) + len(para) > CHUNK_MAX_CHARS:
            chunks.append(current)
            current = para
        else: 
            current = f"{current}\n\n{para}" if current else para 
    if current:
        chunks.append(current)
    return chunks