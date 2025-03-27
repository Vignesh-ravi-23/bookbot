import sys
from stats import text_counter, sort_character_counts

def count_words(text: str):
    """Counts the total number of words in the text."""
    words = text.split()
    return len(words)

def main():
    # Check if a file path is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with an error status

    file_path = sys.argv[1]  # Get the book file path from CLI arguments

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    # Process book text
    word_count = count_words(file_contents)
    char_counts = text_counter(file_contents)
    sorted_counts = sort_character_counts(char_counts)

    # Print formatted output
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...\n")
    
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words\n")
    
    print("--------- Character Count -------")
    for entry in sorted_counts:
        print(f"{entry['char']}: {entry['count']}")

    print("============= END ===============")

# Run the program
main()
