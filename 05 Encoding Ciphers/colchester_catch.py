""""Find hidden message in colchester cipher"""
import sys
import string

def main():
    """Load text, solve null cipher"""
    # Load and process message
    filename = 'colchester_message.txt'
    try:
        loaded_message = load_text('.\\05 Encoding Ciphers\\' + filename)
    except IOError as error:
        print(f"{error}. Terminating program")
        sys.exit(1)

    print("\nORIGINAL MESSAGE: ")
    print(f"{loaded_message}\n")

    clean_message = loaded_message.translate(str.maketrans('' , '', string.punctuation))
    print("\nCLEAN MESSAGE: ")
    print(f"{clean_message}\n")

    word_list = clean_message.split()

    while True:     # Get index of letter and starting point from user
        lookahead = input("\nIndex of letter in word and starting point: ")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Please input numbers.", file=sys.stderr)

    # Run function to decode cipher
    solve_null_cipher(word_list, lookahead)

def load_text(filename):
    """Open text file and return as list"""
    with open(filename, encoding="utf-8") as textfile:
        return textfile.read().strip()

def solve_null_cipher(message, input_index):
    """Solve a null cipher based on index letters in word and starting word.

    message = null cipher text as list without punctuation
    index = where part of cipher is in word and from which word should decryption start
    """
    plaintext = ''
    index = input_index - 1
    counter = index
    out_of_bounds = False
    for word in message[index:]:
        if counter == index:
            if index < len(word):
                plaintext += (word[index])
                counter = 0
            else:
                out_of_bounds = True
                break
        else:
            counter += 1

    if out_of_bounds:
        print("Index is bigger than length of some words", file=sys.stderr)
    else:
        print(f"Using offset of {input_index}: {plaintext}")

if __name__ == '__main__':
    main()
