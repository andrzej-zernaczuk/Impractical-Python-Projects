""""Program that takes a word as input and uses indexing and slicing
to return its Pig Latin equivalent"""
import sys

def main():
    """Check first letter and then proceed with algorithm"""
    vovels=("a", "e", "i", "o", "u", "y")

    while True:
        word=input("input word to be converted to pig latin:\n")
        letters_list=list(word)
        pig_latin_word=""
        if letters_list[0] in vovels:
            pig_latin_final_word=word+'way'
        else:
            move_letter=letters_list.pop(0)
            for letter in letters_list:
                pig_latin_word+=letter
            pig_latin_final_word=pig_latin_word+move_letter+'ay'
        print(pig_latin_final_word)

        try_again=input("\nWanna try again? (Press enter else n to stop)\n ")
        if try_again.lower()=="n":
            sys.exit()

if __name__=="__main__":
    main()
