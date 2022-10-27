"""Find palindromes in a dictionary file"""
import load_dictionary

word_list=load_dictionary.load('.\\02 Finding Palingrams\\recursive_check.txt')
pali_list=[]

def ispalindrome(word_to_check):
    """Checks whether the word is palindrome using recursive approche"""
    if len(word_to_check)<2:
        return True
    if word_to_check[0]!=word_to_check[-1]:
        return False
    return ispalindrome(word_to_check[1:-1])

for word in word_list:
    if ispalindrome(word):
        pali_list.append(word)

print(f"\nNumber of palindromes found = {len(pali_list)}")
print(*pali_list, sep='\n')
