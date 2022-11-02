"""Find anagrams of given name"""
import sys
from collections import Counter
import load_dictionary

dict_file = load_dictionary.load('.\\03 Finding Anagrams\\2of4brif.txt')

dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

initial_name = input("Enter a name: ")

def main():
    """Help user build anagram phrase from their name."""
    name = ''.join(initial_name.lower().split())
    name = name.replace('-', '')

    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print(f"Lenght of anagram phrase = {len(temp_phrase)}")

            find_anagrams(name, dict_file)
            print("Current anagram phrase =", end=" ")
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + ' '
        elif len(temp_phrase) == limit:
            print("\n*****FINISHED!!!*****\n")
            print("Anagram of name =", end=" ")
            print(f"{phrase}\n", file=sys.stderr)

            try_again = input('\n\nTry again? (Press Enter or "n" to quit)\n ')
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()

def find_anagrams(name, word_list):
    """Read name, dictionary file and display all anagrams in name."""
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)

    print(*anagrams, sep='\n')
    print()
    print(f"Remaining letters = {name}")
    print(f"Number of remaining letters = {len(name)}")
    print(f"Number of remaining (real word) anagrams = {len(anagrams)}")

def process_choice(name):
    """Check user choice for validity, return choice and leftover letters."""
    while True:
        choice = input('\nMake a choice else press Enter to start over or # to end: ')
        if choice == '':
            pass
            #main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Won't work! Make another choice!", file=sys.stderr)
    name = ''.join(left_over_list)
    return choice, name

if __name__ == '__main__':
    main()
