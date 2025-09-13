import sys
import string
from stats import get_num_words

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_report(sys.argv[1])

def get_book_content(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(input_str: str):
    word_list = input_str.split()

    return len(word_list)

def count_characters(input_str: str):
    alphabet = string.ascii_lowercase
    input_str = input_str.lower()
    characters_dict = {}
    for i in input_str:
        if i not in characters_dict and i in alphabet:
            characters_dict[i] = 1
        elif i in characters_dict and i in alphabet:
            characters_dict[i] += 1
        else:
            continue

    return characters_dict

def book_report(filepath):
    book = get_book_content(filepath)

    word_count = get_num_words(book)
    character_count = count_characters(book)
    characters = []
    values = []
    for pairs in character_count.items():
        characters.append(pairs[0])
        values.append(pairs[1])

    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document")
    print("\n")

    while len(values) > 0:
        i = values.index(max(values))
        print(f"{characters[i]}: {values[i]}")
        characters.remove(characters[i])
        values.remove(values[i])

    print("--- End report ---")
    return None

if __name__ == "__main__":
    main()
