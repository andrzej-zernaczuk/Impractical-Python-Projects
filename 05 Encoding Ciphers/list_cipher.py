"""Embeds a null cipher within a list of dict words under the deception of vocabulary training"""
from random import randint
import string
import load_dictionary

def main():
    """Take input, load file with dictionary and create vocab list with hidden message"""
    # Write a short message that DOESN'T contain punctuation or numbers!
    input_message = "Panel at east end of chapel slides"

    message =''
    for char in input_message:
        if char in string.ascii_letters:
            message += char
    print(message, "\n")
    message = "".join(message.split())

    # Open dictionary file
    word_list = load_dictionary.load('.\\05 Encoding Ciphers\\2of4brif.txt')

    # Build vocabulary word list with hidden message
    vocab_list = []
    for letter in message:
        size = randint(6, 10)
        for word in word_list:
            if len(word) == size and word[2].lower() == letter.lower() and word not in vocab_list:
                vocab_list.append(word)
                break

    if len(vocab_list) < len(message):
        print("Word list is too small. Try larger dictionary or shorter message")
    else:
        print("Vocabulary words for Unit 1: \n", *vocab_list, sep="\n")

if __name__ == '__main__':
    main()
