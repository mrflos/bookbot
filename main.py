def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"Number of words in {book_path}: {get_words_number(text)}")
    print()
    # print(f"Number of chars in {book_path}: {get_chars_dict(text)}")
    print_chars_dict_sorted(get_chars_dict(text))
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_words_number(text):
    words = text.split()
    return len(words)


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
            print(f"The '{i}' character was found {c} times")
    return


main()
