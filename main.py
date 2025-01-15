import string

def main():
    book_report("books/frankenstein.txt")

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

    word_count = count_words(book)
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
        print(f"The '{characters[i]}' character was found '{values[i]}' times")
        characters.remove(characters[i])
        values.remove(values[i])

    print("--- End report ---")
    return None

if __name__ == "__main__":
    main()
