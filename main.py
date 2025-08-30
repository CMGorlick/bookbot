import sys
from stats import count_words
from stats import count_characters
from stats import sort_dict

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count_dict = count_characters(text)
    sorted_character_dict = sort_dict(character_count_dict)
    sorted_only_letters = [i for i in sorted_character_dict if i["char"].isalpha()]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_only_letters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()