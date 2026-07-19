"""Data layer: all SQLite code. Nobody else writes SQL — they call these functions."""
import json
import sqlite3

from src.config import DB_PATH


def _connect():
    return sqlite3.connect(DB_PATH)


def init_db():
    """Create the chunks table once. Safe to re-run."""
    with _connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS chunks (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                source    TEXT NOT NULL,      -- which document this came from
                content   TEXT NOT NULL,      -- the chunk text
                embedding TEXT NOT NULL       -- the vector, JSON-encoded
            )
        """)


def insert_chunk(source: str, content: str, embedding: list[float]):
    """Save one chunk + its vector. The vector becomes JSON text."""
    with _connect() as conn:
        conn.execute(
            "INSERT INTO chunks (source, content, embedding) VALUES (?, ?, ?)",
            (source, content, json.dumps(embedding)),
        )


def get_all_chunks() -> list[dict]:
    """Return every chunk as a dict: {source, content, embedding(list)}."""
    with _connect() as conn:
        rows = conn.execute(
            "SELECT source, content, embedding FROM chunks"
        ).fetchall()
    return [
        {"source": row[0], "content": row[1], "embedding": json.loads(row[2])}
        for row in rows
    ]
