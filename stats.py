def word_counter(book_string: str):
    words = book_string.split()
    return f"{len(words)} words found in the document"

def text_counter(text: str):
    """Counts the occurrences of each character in the text (case-insensitive)."""
    text = text.lower()  # Convert text to lowercase
    total = {}  # Dictionary to store character counts

    for char in text:
        if char in total:
            total[char] += 1
        else:
            total[char] = 1

    return total  # Return the dictionary of character counts


def sort_character_counts(char_counts: dict):
    """Sorts character counts in descending order and returns a list of dictionaries."""
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():  # Only include letters (skip spaces, punctuation, numbers)
            sorted_list.append({"char": char, "count": count})

    # Sort list of dictionaries by 'count' in descending order
    sorted_list.sort(key=lambda x: x["count"], reverse=True)

    return sorted_list  # Return the sorted list




    return total  # Returns the dictionary 