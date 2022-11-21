""""Find hidden message in null cipher"""
import sys
import string

def main():
    """Load text, solve null cipher"""
    # Load and process message
    filename = input("\nEnter full filename for message to translate: ")
    try:
        loaded_message = load_text('.\\05 Encoding Ciphers\\' + filename)
    except IOError as error:
        print(f"{error}. Terminating program")
        sys.exit(1)

    print("\nORIGINAL MESSAGE: ")
    print(f"{loaded_message}\n")
    print(f"\nList of punctuation marks to check: {string.punctuation}")

    message = ''.join(loaded_message.split()) # Remove whitespaces

    while True:     # Get range of possible cipher keys from user
        lookahead = input("\nNumber of letters to check after punctuation mark: ")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Please input a number.", file=sys.stderr)

    # Run function to decode cipher
    solve_null_cipher(message, lookahead)

def load_text(filename):
    """Open text file and return as list"""
    with open(filename, encoding="utf-8") as textfile:
        return textfile.read().strip()

def solve_null_cipher(message, lookahead):
    """Solve a null cipher based on number of letters after punctuation mark.

    message = null cipher text as string stripped of whitespace
    lookahead = endpoint of range of letters after punctuation mark to examine
    """
    for i in range(1, lookahead + 1):
        plaintext = ''
        counter = 0
        found_first = False
        for char in message:
            if char in string.punctuation:
                counter = 0
                found_first = True
            elif found_first is True:
                counter += 1
            if counter == i:
                plaintext += char
        print(f"Using offset of {i} after punctuation {plaintext}")

if __name__ == '__main__':
    main()
