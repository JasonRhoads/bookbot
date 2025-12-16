def get_book_text(file_path):
    if isinstance(file_path, str):
        with open(file_path) as f:
            return f.read() 


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {len(book_text.split())} total words")

main()