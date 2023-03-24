# Open the file for reading

with open('/home/white/Adarsh/Local-dev-enviroment/bookbot/books/franklin.txt', 'r') as f:

    # Read the entire contents of the file

    file_contents = f.read()

# Print the contents to the console

print(file_contents)

# A function that count the words
def count_words(text):
    # Split the text into words using whitespace as the delimiter
    words = text.split()

    # Return the number of words
    return len(words)

num_words = count_words(file_contents)

print("This file contains",num_words,"words")\




def count_chars(text):
    # Convert all characters to lowercase
    text = text.lower()

    # Create an empty dictionary to store the counts
    counts = {}

    # Iterate over each character in the text
    for char in text:
        # If the character is not a letter, skip it
        if not char.isalpha():
            continue

        # If the character is not already in the dictionary, add it
        if char not in counts:
            counts[char] = 0

        # Increment the count for the character
        counts[char] += 1

    # Return the dictionary of counts
    return counts

    # Count the number of occurrences of each character in the file contents
char_counts = count_chars(file_contents)

# Print the counts to the console
for char, count in char_counts.items():
    print("The",char, "character was found", count,"times")

