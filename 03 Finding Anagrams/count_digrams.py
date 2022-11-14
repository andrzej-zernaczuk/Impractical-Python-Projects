"""Generate letter pairs in given string & find their frequency in a dictionary"""
import re
from collections import defaultdict
from itertools import permutations
import load_dictionary

word_list = load_dictionary.load('.\\03 Finding Anagrams\\2of4brif.txt')

name = input("Input the word you would like to check for digrams: ")
name = name.lower()

digrams = set()
perms = {''.join(i) for i in permutations(name)}
for perm in perms:
    for i in range(0, len(perm) - 1):
        digrams.add(perm[i] + perm[i+1])
print(*sorted(digrams), sep='\n')
print(f"\nNumber of digrams: {len(digrams)}")

mapped = defaultdict(int)
for word in word_list:
    word = word.lower()
    for digram in digrams:
        for m in re.finditer(digram, word):
            mapped[digram] += 1

print("Digram frequency count: ")
count = 0
for k in sorted(mapped):
    print(f"{k} {mapped[k]}")
    