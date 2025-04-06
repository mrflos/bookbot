import sys
from stats import get_num_words

def main():
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    # print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_num_words(text)} words found in the document")
    print()
    # print(f"Number of chars in {book_path}: {get_chars_dict(text)}")
    print_chars_dict_sorted(get_chars_dict(text))
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def print_chars_dict_sorted(chars):
    chars = sorted(chars.items())
    for i, c in chars:
        if i.isalpha():
            print(f"{i}: {c}")
    return


main()
