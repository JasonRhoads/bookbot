from stats import get_num_words, count_characters

def get_book_text(file_path):
    if isinstance(file_path, str):
        with open(file_path) as f:
            return f.read() 


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {get_num_words(book_text)} total words")
    print(count_characters(book_text))
main()