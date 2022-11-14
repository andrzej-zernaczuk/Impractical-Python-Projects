r"""Encrypt a Civil War 'rail fence' type cypher
This is for the '2-rail' fence cipher for fairly short messages.

Example text to encrypt: 'Buy more Maine potatoes'

Rail fence style: B Y O E A N P T T E
                   U M R M I E O A O S

Read zigzag: \/\/\/\/\/\/\/\/\/\/

Encrypted: BYOEA NPTTE UMRMI EOSOS

"""
# ========================================================================================
# USER INPUT:

# The string to be encrypted (paste between triple-quotes)
original_message = """Let us cross over the river and rest under the shade of the trees"""

# END OF USER INPUT
# ========================================================================================

def main():
    """Run program to encryp message using 2-rail fence cipher"""
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
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds

    return rails

def encrypt(rails):
    """Split letters in ciphertext into chunks of 5 & join to make string"""
    ciphertext = ' '.join([rails[i:i+5] for i in range (0, len(rails), 5)])
    print(f"ciphertext: {ciphertext}")

if __name__ == '__main__':
    main()
