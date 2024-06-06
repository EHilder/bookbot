def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    return file_contents   
full_text = main()

def wordcount(full_text):
    words = full_text.split()
    word_count = 0
    for word in words:
        word_count += 1
    print(word_count)
wordcount(full_text)

def character_count(full_text):
    lowered_string = full_text.lower()
    letter_dictionary = {}
    for letter in lowered_string:
        if letter != " ":
            if letter in letter_dictionary:
                letter_dictionary[letter] += 1
            else:
                letter_dictionary[letter] = 1
    print(letter_dictionary)

    

character_count(full_text)