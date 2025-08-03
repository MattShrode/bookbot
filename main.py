def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_contents):
    file_words = file_contents.split()
    word_count = len(file_words)
    return word_count

def main():
    file_path = 'books/frankenstein.txt'
    file_contents = get_book_text(file_path)
    word_count = get_word_count(file_contents)
    print(f"{word_count} words found in the document")

main()