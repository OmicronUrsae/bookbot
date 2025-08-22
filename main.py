from stats import get_word_count, get_sorted_char_count
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_text(file_path)
    word_count = get_word_count(text)
    sorted_char_count = get_sorted_char_count(text)
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {file_path}...")
    print("-------- Word Count ---------")
    print(f"Found {word_count} total words.")
    print("------ Character Count ------")
    for item in sorted_char_count:
        print(f"{item["char"]}: {item["freq"]}")
    print("============ END ============")


def get_text(file_path): #retrieves the text from a specified file.
    try:
        with open(file_path) as f:
            return f.read()
    except Exception as e:
        print(f"Error: {e}")

main()