from stats import get_word_count
from stats import get_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    file_path = 'books/frankenstein.txt'
    file_contents = get_book_text(file_path)
    word_count = get_word_count(file_contents)
    print(f"{word_count} words found in the document")
    char_count = get_char_count(file_contents)
    print(char_count)

main()