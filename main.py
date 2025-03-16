import sys
from stats import get_num_words, get_num_char, sort_chars


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    contents = get_book_text(sys.argv[1])
    num_words = get_num_words(contents)
    num_chars = get_num_char(contents)
    sorted_chars = sort_chars(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}.")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["character"].isalpha():
            print(f"{char["character"]}: {char["count"]}")

main()
