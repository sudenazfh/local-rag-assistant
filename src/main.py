from src.generator import answer_query
import os

def main():
    print("Local RAG Assistant. Type 'quit' to exit.\n")
    while True:
        try:
            question = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            os._exit(0)
            break
        if question.lower() in {"quit", "exit"}:
            break
        if not question:
            continue
        print("\nAssistant: ", answer_query(question), "\n")
        
if __name__ == "__main__":
    main()