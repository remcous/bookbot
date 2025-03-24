from stats import get_num_words
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)

    word_count = get_num_words(book)
    char_dict = get_letter_count(book)
    sorted_chars = sort_letters_dict(char_dict)

    # Print report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for entry in sorted_chars:
        print(f"{entry['letter']}: {entry['count']}")
    print("--- End report ---")


def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

if __name__ == '__main__':
    main()