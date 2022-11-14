"""Encrypt the message with a Union Route Cipher.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, dummy words, code words

Prints translated plaintext
"""
import sys
import string

# ========================================================================================
# USER INPUT

# The string to be decrypted (input between triple-quotes):
message = """We will run the batteries at Vicksburg the night of April 16 and \
proceed to Grand Gulf where we will reduce the forts. \
Be prepared to cross the river on April 25 or 29. Admiral Porter."""

# Number of columns in transpositon matrix:
COLS = 6

# Number of rows in the transpsition matrix:
ROWS = 7

# Code words:
code_words = {'BATTERIES':'HOUNDS',
              'VICKSBURG':'ODOR',
              'APRIL':'CLAYTON',
              '16':'SWEET',
              'GRAND':'TREE',
              'GULF':'OWL',
              'FORTS':'BAILEY',
              'RIVER':'HICKORY',
              '25':'MULTIPLY',
              '29':'ADD',
              'ADMIRAL':'HERMES',
              'PORTER':'LANGFORD'}

# Dummy words:
dummy_words = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur']

# Encryption key:
encryption_key = """ -1 3 -2 6 5 -4 """

# END OF USER INPUT
# ========================================================================================

def main():
    """Run program and print encrypted message"""
    # Strip all the punctation marks
    message_stripped = message.translate((str.maketrans('', '', string.punctuation)))
    word_list = list(message_stripped.split())      # Split by spaces
    word_list = [i.upper() for i in word_list]      # UPPER CASE for obscuring begining of sentence
    word_list_substituted = substitute_words(word_list)
    for word in dummy_words:                        # Append dummy words to message
        word_list_substituted.append(word.upper())
    validate_col_row(word_list_substituted)
    key_int = key_to_int(encryption_key)
    encryption_matrix = build_matrix(word_list_substituted)
    encrypted_message = encrypt(key_int, encryption_matrix)

    # print(f"\nOriginal message: {message}")
    print(f"Encrypted message: {encrypted_message}")

def substitute_words(message_list):
    """Substitue chosen words for code words to obscure the message"""
    word_list_substituted = []
    for word in message_list:
        if word in code_words:
            word_list_substituted.append(code_words.get(word))
        else:
            word_list_substituted.append(word)

    return word_list_substituted

def validate_col_row(word_list_prepared):
    """Check validity of input of columns & rows vs. message lenght"""
    factors = []
    len_message = len(word_list_prepared)
    for i in range(2, len_message): # range excludes 1-column matrix
        if len_message % i == 0:
            factors.append(i)

    print(f"\nLength of message: {len_message}")
    print(f"Acceptable column/row values include: {factors}\n")

    if ROWS * COLS != len_message:
        print("\nError - Input columns & rows not factors of length "
              "of message. Terminating program.", file=sys.stderr)
        sys.exit(1)

def key_to_int(key):
    """Turn key into list of ints $ check validity"""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS or 0 in key_int:
        print("\nError - Problem with key. Terminating", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int

def build_matrix(word_list_prepared):
    """Turn every n items in a list into a new item in a list of lists"""
    encryption_matrix = [None] * ROWS
    start = 0
    stop = COLS
    rows_counter = 1
    while rows_counter <= ROWS:
        col_items = word_list_prepared[start:stop]
        encryption_matrix[rows_counter - 1] = col_items
        start += COLS
        stop += COLS
        rows_counter += 1

    return encryption_matrix

def encrypt(key, matrix_prepared):
    """Loop through nested lists popping of last item to a string"""
    encrypted_message = ''
    for key_part in key:
        if key_part < 0:
            for i in reversed(range(7)):
                encrypted_message += matrix_prepared[i][abs(key_part) - 1] + ' '
        if key_part > 0:
            for i in range(7):
                encrypted_message += matrix_prepared[i][key_part - 1] + ' '

    return encrypted_message

if __name__ == '__main__':
    main()
