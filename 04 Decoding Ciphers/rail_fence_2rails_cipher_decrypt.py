r"""Decrypt a Civil War 'rail fence' type cipher.
This is for a 2-rail fence cipher for short messages.

Example plaintext: 'Buy more Maine potatoes'

Rail fence style: B Y O E A N P T T E
                   U M R M I E O A O S

Read zigzag: \/\/\/\/\/\/\/\/\/\/

Ciphertext: BYOEA NPTTE UMRMI EOSOS

"""
import math
import itertools

# ========================================================================================
# USER INPUT:

# The string to be decrypted (paste between triple-quotes)
encrypted_message = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES"""

# END OF USER INPUT
# ========================================================================================

def main():
    """Run program to decrypt 2-rail fence cipher"""
    message = prep_ciphertext(encrypted_message)
    row1, row2 = split_rails(message)
    decrypt(row1, row2)

def prep_ciphertext(ciphertext):
    """Remove whitespaces"""
    message = "".join(ciphertext.split())
    print(f"\nCiphertext: {ciphertext}\n")

    return message

def split_rails(message):
    """Split message in two, alwyas round up for 1st row"""
    row_1_len = math.ceil(len(message)/2)
    row1 = (message[:row_1_len]).lower()
    row2 = (message[row_1_len:]).lower()

    return row1, row2

def decrypt(row1, row2):
    """Build list with every other letter in 2 strings"""
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1)
        plaintext.append(r2)
    if None in plaintext:
        plaintext.pop()

    print(f"rail_1: {row1}")
    print(f"rail_2: {row2}")
    print(f"\nPlaintext: {''.join(plaintext)}")

if __name__ == '__main__':
    main()
