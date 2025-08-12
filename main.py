from stats import get_word_count
from stats import get_char_count
from stats import get_list_of_dict
from stats import sort_on
import sys

def program_start():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(sorted_list_of_char_count, file_path, word_count):
    print("""============ BOOKBOT ============\n"""
          f"""Analyzing book found at {file_path}...\n"""
          """----------- Word Count ----------\n"""
          f"""Found {word_count} total words\n"""
          """--------- Character Count -------""")
    for dict in sorted_list_of_char_count:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")
        

def main():
    program_start()
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    word_count = get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    list_of_char_count = get_list_of_dict(char_count)
    list_of_char_count.sort(reverse=True, key=sort_on)
    print_report(list_of_char_count, file_path, word_count)

main()