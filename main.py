# Import functions
from stats import count_words, count_chars, sort_chars
import sys


# Fetching file path from user and return contents of book.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
        return str(book_text)


# Main block
def main(path_to_file):
    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    num_chars = count_chars(book_text)
    sorted_chars = sort_chars(num_chars)
    print(f'''
============ BOOKBOT ============
Analyzing book found at {path_to_file}
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
''')
    for char in sorted_chars:
        print(f"{char}: {sorted_chars[char]}")
    print("\n============= END ===============\n")



if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    args = sys.argv
    main(args[1])