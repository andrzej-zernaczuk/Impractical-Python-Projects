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

# The string to be decrypted (paste between triple-quotes)
encrypted_message = """LSSEE EDTEE DTREU COSVR HRVRN RSUDR HSAEF HTEST ROTIA ENTHO EE"""

# Number of rails
rails_num = 3

# END OF USER INPUT
# ========================================================================================

def main():
    """Run program to decrypt 3-rail fence cipher"""
    message = prep_ciphertext(encrypted_message)
    row1, row2, row3= split_rails(message)
    decrypt(row1, row2, row3)

def prep_ciphertext(ciphertext):
    """Remove whitespaces"""
    message = "".join(ciphertext.split())
    print(f"\nCiphertext: {ciphertext}")
    return message

def split_rails(message):
    """Split message in three"""
    message_length = len(message)
    border_rails_length = int(message_length/(2*(rails_num -1))) # Length of 1st and last rail
    middle_rails_length = int(2 * border_rails_length)

    row1 = list((message[:border_rails_length]).lower())
    row2 = list((message[border_rails_length:border_rails_length+middle_rails_length]).lower())
    row3 = list((message[border_rails_length+middle_rails_length:]).lower())
    return row1, row2, row3

def decrypt(row1, row2, row3):
    """Decrypt the 3 rail cipher"""
    plaintext = []

    for i in range(0, len(row1)):
        plaintext.append(row1.pop(0))
        plaintext.append(row2.pop(0))
        plaintext.append(row3.pop(0))
        plaintext.append(row2.pop(0))
        i += 1

    print(f"\nPlaintext: {''.join(plaintext)}")

if __name__ == '__main__':
    main()
