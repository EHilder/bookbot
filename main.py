def main():
    with open("books/frankenstein.txt") as f:
        return f.read()   
text = main()

def wordcount(text):
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count
word_count = wordcount(text)

def character_count(text):
    letter_dictionary = {}
    for letter in text.lower():
        if not letter.isspace():
            if letter in letter_dictionary:
                letter_dictionary[letter] += 1
            else:
                letter_dictionary[letter] = 1
    return letter_dictionary
letter_dictionary = character_count(text)

print(f"--- Begin report of books/frankenstein.txt ---\n")
print(f"{word_count} words found in the document")
for letter, count in letter_dictionary.items():
    print(f"The '{letter}' character was found {count} times")