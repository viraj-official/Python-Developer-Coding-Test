def count_word_in_file(filename: str) -> int:
    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)

print(count_word_in_file("sample.txt"))
