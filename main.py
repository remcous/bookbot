def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)

    word_count = get_num_words(book)
    char_dict = get_letter_count(book)
    sorted_chars = sort_letters_dict(char_dict)

    # Print report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for entry in sorted_chars:
        print(f"The '{entry['letter']}' character was found {entry['count']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path, "r") as f:
        return f.read()
    
def get_num_words(book):
    return len(book.split())

def get_letter_count(book):
    letters = {}
    for letter in book.lower():
        if letter.isalpha():
            letters[letter] = letters.get(letter, 0) + 1
    return letters

def sort_letters_dict(dict):
    def sort_on(dict):
        return dict["count"]
    
    lst = [{"letter": k, "count": v} for k,v in dict.items()]
    lst.sort(reverse=True, key=sort_on)
    return lst

if __name__ == '__main__':
    main()