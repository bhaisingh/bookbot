def get_book_word_count(book_text):
    """
    Counts the number of words in the book text.
    
    Args:
        book_text (str): The content of the book.
        
    Returns:
        int: The word count of the book text.
    """
    return len(book_text.split())

def get_book_character_count(book_text):
    """
    Counts the number of characters in the book text.
    
    Args:
        book_text (str): The content of the book.
        
    Returns:
        int: The character count of the book text.
    """
    char_count = {}
    for char in book_text:
        # Ignore if not a letter
        if not char.isalpha():
            continue
        else:
            char_lower = char.lower()
            if char_lower in char_count:
                char_count[char_lower] += 1
            else:
                char_count[char_lower] = 1

    return char_count

def sort_on(char_dict):
    """
    Sorts a dictionary by its values in descending order.
    
    Args:
        char_dict (dict): The dictionary to sort.
        
    Returns:
        dict: The sorted dictionary.
    """
    return char_dict[1]



def print_report(book_text):
    """
    Prints a report of the book statistics including word count and character count.
    
    Args:
        book_text (str): The content of the book.
    """
    word_count = get_book_word_count(book_text)
    char_count = get_book_character_count(book_text)
    items = char_count.items()
    #print("items:", items)
    items_list = list(items)
    #print("items_list:", items_list)
   
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # sort the character count dictionary by count
    #char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)    
    
    sorted_items = sorted(items_list, key=sort_on, reverse=True)
    sorted_dict = dict(sorted_items)

    for char, count in sorted_dict.items():
        print(f"{char}: {count}")
    print("============= END ===============")
