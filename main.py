import sys
from stats import word_count, char_count
def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) <= 1:
        print ("Usage: python 3 main.py <path_to_book>")
        sys.exit(1)
    else:
        fpath = sys.argv[1]
        book = get_book_text(fpath)
        word_count_result = word_count(book)
        char_count_result = char_count(book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {fpath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count_result} total words")
        print("--------- Character Count -------")
        for char_dict in char_count_result:
            for char, count in char_dict.items():
                if char.isalpha():
                    print(f"{char}: {count}")
    
        print("============= END ===============")

main()