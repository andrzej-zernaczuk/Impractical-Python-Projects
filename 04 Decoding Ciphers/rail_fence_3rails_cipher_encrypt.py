r"""Encrypt a Civil War 'rail fence' type cypher
This is for the '3-rail' fence cipher for fairly short messages.

Example text to encrypt: 'Buy more Maine potatoes'

Rail fence style: B   O   A   P   T
                   U M R M I E O A O S
                    Y   E   N   T   E

Read zigzag: \  /\  /\  /
              \/  \/  \/

Encrypted: BOAPT UMRMI EOAOS YENTE

"""
# ========================================================================================
# USER INPUT:

# The string to be encrypted (paste between triple-quotes)
original_message = """Let us cross over the river and rest under the shade of the trees"""

# END OF USER INPUT
# ========================================================================================

def main():
    """Run program to encryp message using 3-rail fence cipher"""
    message = prep_plaintext(original_message)
    rails = build_rails(message)
    encrypt(rails)

def prep_plaintext(plaintext):
    """Remove spaces & leading/trailing whitespaces"""
    message = "".join(plaintext.split())
    message = message.upper() #obscure start of the sentence and names
    print(f"\nplaintext: {plaintext}")

    return message

def build_rails(message):
    """Build strings with every other letter in message"""
    first_row = message[::4]
    second_row = message[1::2]
    third_row = message[2::4]
    print(first_row)
    print(second_row)
    print(third_row)

    rails = first_row + second_row + third_row

    return rails

def encrypt(rails):
    """Split letters in ciphertext into chunks of 5 & join to make string"""
    ciphertext = ' '.join([rails[i:i+5] for i in range (0, len(rails), 5)])
    print(f"ciphertext: {ciphertext}")

if __name__ == '__main__':
    main()
