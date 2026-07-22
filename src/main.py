import os

from src.generator import answer_query

os.system("")  # enable ANSI color codes 

AMBER = "\033[38;2;255;176;0m"   
TEAL = "\033[38;2;0;190;200m"    
PINK = "\033[38;2;255;70;120m"   
DIM = "\033[38;2;120;120;140m"   
RESET = "\033[0m"


def main():
    print(f"{AMBER}Local RAG Assistant{RESET} {DIM}— type 'quit' to exit{RESET}\n")
    while True:
        try:
            question = input(f"{TEAL}You (ask a question...): {RESET}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{PINK}Goodbye!{RESET}")
            break
        if question.lower() in {"quit", "exit"}:
            print(f"{PINK}Goodbye!{RESET}")
            break
        if not question:
            continue
        print(f"\n{AMBER}Assistant:{RESET} {answer_query(question)}\n")


if __name__ == "__main__":
    main()
