from src.database import init_db, insert_chunk, get_all_chunks

init_db()
insert_chunk("t", "hi", [0.1, 0.2])
print(get_all_chunks())