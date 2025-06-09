import sys
from stats import string_word_count
from stats import character_count
from stats import sorted_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        book_text = get_book_text(filepath)
        num_words = string_word_count(book_text)
        char_count = character_count(book_text)
        sorted_dictionary = sorted_dicts(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_dictionary:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

main()