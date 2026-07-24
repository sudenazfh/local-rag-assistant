import json
import sqlite3

from src.config import DB_PATH


def _connect():
    return sqlite3.connect(DB_PATH)


def init_db():
    with _connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS chunks (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                source    TEXT NOT NULL,      
                content   TEXT NOT NULL,      
                embedding TEXT NOT NULL       
            )
        """)


def insert_chunk(source: str, content: str, embedding: list[float]):
    with _connect() as conn:
        conn.execute(
            "INSERT INTO chunks (source, content, embedding) VALUES (?, ?, ?)",
            (source, content, json.dumps(embedding)),
        )


def get_all_chunks() -> list[dict]:
    with _connect() as conn:
        rows = conn.execute(
            "SELECT source, content, embedding FROM chunks"
        ).fetchall()
    return [
        {"source": row[0], "content": row[1], "embedding": json.loads(row[2])}
        for row in rows
    ]
