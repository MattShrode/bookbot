def get_word_count(file_contents):
    file_words = file_contents.split()
    word_count = len(file_words)
    return word_count

def get_char_count(file_contents):
    file_contents_lower = file_contents.lower()
    char_count = {}
    for char in file_contents_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count