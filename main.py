import sys
from stats import get_num_words, count_characters, sorted_dictionaries


def get_book_text(file_path):
    if isinstance(file_path, str):
        with open(file_path) as f:
            return f.read() 


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    character_list = sorted_dictionaries(count_characters(book_text))
    for character in character_list:
        print(f'{character["char"]}: {character["num"]}')

    print("============= END ===============")
main()