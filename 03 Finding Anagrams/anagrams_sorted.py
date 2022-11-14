"""Find anagrams of given word in a dictionary file"""
import time
import load_dictionary

word_list = load_dictionary.load('.\\03 Finding Anagrams\\2of4brif.txt')
anag_list = []

name = input("Enter word or name to find anagram: ")
print(f"Input name: {name}")
name = name.lower()
print(f"Using name: {name}")

start_time = time.time()

name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anag_list.append(word)

end_time = time.time()

if len(anag_list) == 0:
    print("You need new name or a larger dictionary!")
else:
    print("Anagrams found:", *anag_list, sep='\n')

print(f"Process took: {end_time - start_time}")
