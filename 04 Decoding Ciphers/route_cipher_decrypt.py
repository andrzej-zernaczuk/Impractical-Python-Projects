"""Decrypt a path through a Union Route Cipher.

Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top & read down.

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

Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext
"""
import sys

# ========================================================================================
# USER INPUT

# The string to be decrypted (input between triple-quotes):
ciphertext = """LOREM CLAYTON PREPARED WE AND ODOR WE RUN NIGHT TO REDUCE CROSS OR DOLOR IPSUM MULTIPLY TO WILL PROCEED THE WILL AT SWEET WHERE BE ON LANGFORD CONSECTETUR HOUNDS CLAYTON OWL BAILEY HICKORY HERMES AMET SIT ADD THE THE TREE OF THE"""

# Number of columns in transpositon matrix:
COLS = 6

# Number of rows in the transpsition matrix:
ROWS = 7

# Key with spaces between numbers, negative to read UP (ex = -1 2 -3 4):
decryption_key = """ -1 3 -2 6 5 -4 """

# END OF USER INPUT
# ========================================================================================

def main():
    """Run program and print decrypted plaintext"""
    print(f"\nCiphertext: {ciphertext}")
    print(f"Trying: {COLS} columns")
    print(f"Trying: {ROWS} rows")
    print(f"Trying key: {decryption_key}")

    # Split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(decryption_key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print(f"Original message: {plaintext}")

def validate_col_row(cipherlist):
    """Check validity of input of columns & rows vs. message lenght"""
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher): # range excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)

    print(f"\nLength of cipher: {len_cipher}")
    print(f"Acceptable column/row values include: {factors}\n")

    if ROWS * COLS != len_cipher:
        print("\nError - Input columns & rows not factors of length "
              "of cipher. Terminating program.", file=sys.stderr)
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

def build_matrix(key_int, cipherlist):
    """Turn every n items in a list into a new item in a list of lists"""
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS
    for key_part in key_int:
        if key_part < 0:
            col_items = cipherlist[start:stop]
        if key_part > 0:
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(key_part) - 1] = col_items
        start += ROWS
        stop += ROWS

    return translation_matrix

def decrypt(translation_matrix):
    """Loop through nested lists popping of last item to a string"""
    plaintext = ''
    for row in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '

    return plaintext

if __name__ == '__main__':
    main()
