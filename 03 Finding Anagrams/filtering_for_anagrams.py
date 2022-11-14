"""Find permutations of given string in a dictionary file using filters"""
import sys
from itertools import permutations
from collections import Counter
import load_dictionary

def main():
    """Load files, run filters, allow user to view anagrams by 1st letter."""
    name = input("Input the word you would like to check for anagrams: ")
    name = name.lower()

    word_list_ini = load_dictionary.load('.\\03 Finding Anagrams\\2of4brif.txt')
    trigrams_filtered = load_dictionary.load('.\\03 Finding Anagrams\\least-likely_trigrams.txt')

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map = cv_map_words(word_list)
    filter_1 = cv_map_filter(name, filtered_cv_map)
    filter_2 = trigrams_filter(filter_1, trigrams_filtered)
    filter_3 = letter_pair_filter(filter_2)
    view_by_letter(name, filter_3)

def prep_words(name, word_list_ini):
    """Prep word list for finding anagrams."""
    print(f"Length of initial_word_list: {len(word_list_ini)}")

    len_name = len(name)
    word_list = [word.lower() for word in word_list_ini if len(word)  == len_name]
    print(f"Lenght of new_word_list: {len(word_list)}")

    return word_list

def cv_map_words(word_list):
    """Map letters in words to consonants & vowels."""
    vowels = 'aeiouy'

    cv_mapped_words = []
    for word in word_list:
        temp = ''
        for letter in word:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'

        cv_mapped_words.append(temp)

    # determine number of UNIQUE c-v patterns
    total = len(set(cv_mapped_words))
    # target fraction to eliminate
    target = 0.05
    # get number of items in target fraction
    items_num = int(total * target)

    count_pruned = Counter(cv_mapped_words).most_common(total - items_num)

    filtered_cv_map = set()
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print(f"Length of filtered_cv_map: {filtered_cv_map}")

    return filtered_cv_map

def cv_map_filter(name, filtered_cv_map):
    """Remove permutations of words based on unlikely cons-vowel combos."""
    vowels = 'aeiouy'

    perms = {''.join(i) for i in permutations(name)}
    print(f"Length of initial permutations set: {len(perms)}")

    filter_1 = set()
    for candidate in perms:
        temp = ''
        for letter in candidate:
            if letter in vowels:
                temp += 'v'
            else:
                temp += 'c'
        if temp in filtered_cv_map:
            filter_1.add(candidate)
    print(f"# of choices after filter_1: {len(filter_1)}")

    return filter_1

def trigrams_filter(filter_1, trigrams_filtered):
    """Remove unlikely trigrams from permutations."""
    filtered = set()
    for candidate in filter_1:
        for triplet in trigrams_filtered:
            triplet = triplet.lower()
            if triplet in candidate:
                filtered.add(candidate)
    filter_2 = filter_1 - filtered
    print(f"# of choices after filter_2: {len(filter_2)}")

    return filter_2

def letter_pair_filter(filter_2):
    """Remove unlikely letter-pairs from permutations."""
    filtered = set()
    rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv', 'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
    first_pair_rejects = ['ld', 'lm', 'lt', 'lv', 'rd', 'rl', 'rm', 'rt', 'rv', 'tl', 'tm']
    for candidate in filter_2:
        for reject in rejects:
            if reject in candidate:
                filtered.add(candidate)
        for first_pair_reject in first_pair_rejects:
            if candidate.startswith(first_pair_reject):
                filtered.add(candidate)
    filter_3 = filter_2 - filtered
    print(f"# of choices after filter_3: {len(filter_3)}")

    return filter_3

def view_by_letter(name, filter_3):
    """Filter to anagrams starting with input letter."""
    print(f"Remaining letters: {name}")
    first = input("Select a starting letter or press Enter to see all: ")

    subset = []
    for candidate in filter_3:
        if candidate.startswith(first):
            subset.append(candidate)
    print(*sorted(subset), sep='\n')
    print(f"# of choices starting with '{first}': {len(subset)}")

    try_again = input("Try again? (Press Enter or else any other key to Exit): ")
    if try_again.lower() == '':
        view_by_letter(name, filter_3)
    else:
        sys.exit()

if __name__ == '__main__':
    main()
