from stats import get_book_word_count
from stats import get_book_character_count
from stats import print_report
import sys

def get_book_text(book_filepath):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        book_filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    with open(book_filepath, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    """
    Main function to execute the script.
    """
    # Check if the book file path is provided as a command line argument
    if len(sys.argv) == 2:
        book_filepath = sys.argv[1]
    else:
        # Error message if the file path is not provided
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #book_filepath = 'books/frankenstein.txt'   # Path to the book file
    book_text = get_book_text(book_filepath)
    
    # Print the report of the book statistics
    print_report(book_text)
    
    # Count the number of words in the book text
    #word_count = get_book_word_count(book_text)
    # Count the number of characters in the book text
    #char_count = get_book_character_count(book_text)
       
    # Print the word count
    #print(f"{word_count} words found in the document")      
    # Print the character count
    #print(char_count)
    

if __name__ == "__main__":
    main()

