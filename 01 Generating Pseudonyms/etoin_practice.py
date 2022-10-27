"""Map letters from string into dictionary & print bar chart of frequency."""

import pprint
from collections import defaultdict

TEXT = 'Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same.'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

mapped = defaultdict(list)
for char in TEXT:
    char=char.lower()
    if char in ALPHABET:
        mapped[char].append(char)

print(f"{TEXT}\n")
pprint.pprint(mapped, width=110)
