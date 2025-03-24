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