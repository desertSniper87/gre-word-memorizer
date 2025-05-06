import os
import sys
from word_service import get_word_definition
from image_service import search_image, download_image
from db_service import initialize_db, save_word, get_word, get_all_words

def process_word(word):
    """Process a word by getting its definition and image
    
    Args:
        word (str): The word to process
        
    Returns:
        dict: The processed word data
    """
    print(f"\nProcessing word: {word}")
    
    # Check if word already exists in database
    existing_word = get_word(word)
    if existing_word:
        print(f"Word '{word}' already exists in the database.")
        display_word_info(existing_word)
        return existing_word
    
    # Get word definition
    word_data = get_word_definition(word)
    if not word_data:
        print(f"Could not find definition for '{word}'.")
        return None
    
    # Get an image for the word
    image_data = search_image(word)
    if image_data:
        print(f"Opened browser with Google Images search for '{word}'")
        word_data['image_url'] = image_data['url']
        word_data['image_path'] = f"Manual selection required for '{word}'"
    else:
        print(f"Could not open browser for '{word}'")
    
    # Save to database
    save_word(word_data)
    print(f"Saved '{word}' to database.")
    
    # Display the information
    display_word_info(word_data)
    
    return word_data

def display_word_info(word_data):
    """Display word information in a formatted way
    
    Args:
        word_data (dict): The word data to display
    """
    print("\n" + "-"*50)
    print(f"Word: {word_data['word']}")
    
    if word_data.get('phonetics'):
        print(f"Pronunciation: {word_data['phonetics']}")
    
    if word_data.get('part_of_speech'):
        print(f"Part of Speech: {word_data['part_of_speech']}")
    
    print(f"\nDefinition: {word_data['definition']}")
    
    if word_data.get('example'):
        print(f"\nExample: {word_data['example']}")
    
    if word_data.get('image_path'):
        print(f"\nImage saved at: {word_data['image_path']}")
    elif word_data.get('image_url'):
        print(f"\nImage URL: {word_data['image_url']}")
        if word_data.get('source'):
            print(f"Source: {word_data['source']}")
    
    print("-"*50)

def list_all_words():
    """List all words in the database"""
    words = get_all_words()
    
    if not words:
        print("No words in the database.")
        return
    
    print("\n" + "-"*50)
    print(f"Total words: {len(words)}")
    print("-"*50)
    
    for i, word_data in enumerate(words, 1):
        print(f"{i}. {word_data['word']}")
    
    print("-"*50)

def main():
    """Main function to run the GRE Word Memorizer"""
    # Initialize the database
    initialize_db()
    
    if len(sys.argv) > 1:
        # Process command line arguments
        if sys.argv[1].lower() == "list":
            list_all_words()
        else:
            word = sys.argv[1]
            process_word(word)
    else:
        # Interactive mode
        print("Welcome to GRE Word Memorizer!")
        print("\nCommands:")
        print("  word    - Process a specific word")
        print("  list    - List all saved words")
        print("  exit    - Exit the program")
        
        while True:
            command = input("\nEnter a command or word: ").strip()
            
            if command.lower() == "exit":
                break
            elif command.lower() == "list":
                list_all_words()
            else:
                process_word(command)

if __name__ == "__main__":
    main()