from stats import get_word_count
from stats import get_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_list_of_dict(char_count_dict):
    list_of_char_count = [{"char": key, "num": value} for key, value in char_count_dict.items()]
    return list_of_char_count

def main():
    file_path = 'books/frankenstein.txt'
    file_contents = get_book_text(file_path)
    word_count = get_word_count(file_contents)
    print(f"{word_count} words found in the document")
    char_count = get_char_count(file_contents)
    list_of_char_count = get_list_of_dict(char_count)
    print(list_of_char_count)

main()