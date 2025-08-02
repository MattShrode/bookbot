def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = 'books/frankenstein.txt'

    print(get_book_text(file_path))

main()