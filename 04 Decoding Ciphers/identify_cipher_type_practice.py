"""Load ciphertext & use fraction of ETAOIN present to classify cipher type"""
import sys
from collections import Counter

# set arbitrary cutoff fraction of 6 most common letters in English
# ciphertext with target fraction or greater = transposition cipher
CUTOFF = 0.5

def load(filename):
    """Open text file and return as list"""
    with open(filename, encoding="utf-8") as textfile:
        return textfile.read().strip()

try:
    ciphertext = load('.\\04 Decoding Ciphers\\cipher_b.txt')
except IOError as e:
    print(f"{e}. Terminating program", file=sys.stderr)
    sys.exit(1)

# Count 6 most common letters (ETAOIN) in ciphertext:
six_most_freq = Counter(ciphertext.lower()).most_common(6)
print("\nSix most-frequently-used letters in English = ETAOIN")
print('\nSix most frequent letters in ciphertext =')
print(*six_most_freq, sep='\n')

# Convert list of tuples to set of letters for comparision
cipher_top_6 = {i[0] for i in six_most_freq}

TARGET = 'etaoin'
count = 0
for letter in TARGET:
    if letter in cipher_top_6:
        count +=1

if count/len(TARGET) >= CUTOFF:
    print("\nThis ciphertext most-likely produced by a TRANSPOSITION cipher")
else:
    print("This ciphertext most-likely produced by a SUBSTITUTION cipher")
