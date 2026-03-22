from utils import explain_code, detect_bug, improve_code, review_code, generate_tests, add_docstrings
from tutor import ai_tutor

def get_code_input() -> str:
    print("Paste your code (type END on a new line when done):")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("=" * 40)
    print("   AI Dev Assistant CLI (Claude-powered)")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("  1. Explain Code")
        print("  2. Detect Bug")
        print("  3. Improve Code")
        print("  4. Full Code Review")
        print("  5. Generate Tests")
        print("  6. Add Docstrings")
        print("  7. Ask AI Tutor")
        print("  8. Exit")

        choice = input("\nSelect (1-8): ").strip()

        if choice == "8":
            print("Goodbye!")
            break
        elif choice == "7":
            question = input("Ask your question: ").strip()
            print("\n" + ai_tutor(question))
        elif choice in ("1", "2", "3", "4", "5", "6"):
            code = get_code_input()
            print("\nProcessing...\n")
            if choice == "1":
                print(explain_code(code))
            elif choice == "2":
                print(detect_bug(code))
            elif choice == "3":
                print(improve_code(code))
            elif choice == "4":
                print(review_code(code))
            elif choice == "5":
                print(generate_tests(code))
            elif choice == "6":
                print(add_docstrings(code))
        else:
            print("Invalid choice. Please select 1-8.")

if __name__ == "__main__":
    main()
