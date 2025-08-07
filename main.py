from stats import get_word_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_char_count(file_contents):
    file_contents_lower = file_contents.lower()
    char_count = {}
    for char in file_contents_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)

def main():
    file_path = 'books/frankenstein.txt'
    file_contents = get_book_text(file_path)
    word_count = get_word_count(file_contents)
    print(f"{word_count} words found in the document")
    get_char_count(file_contents)

main()