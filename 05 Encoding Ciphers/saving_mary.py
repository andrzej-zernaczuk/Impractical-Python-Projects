"""Embeds a null cipher within a list of names under the deception of supporters list"""
import secrets
import string
import load_dictionary

def main():
    """Take input, load file with dictionary and create vocab list with hidden message"""
    # Write a short message that DOESN'T contain punctuation or numbers!
    input_message = "Give your word and we shall rise"

    message =''
    for char in input_message:
        if char in string.ascii_letters:
            message += char
    print(message, "\n")
    message = "".join(message.split())

    # Open dictionary file
    names_list = load_dictionary.load('.\\05 Encoding Ciphers\\supporters.txt')

    # Build supporters list with hidden message
    supporter_list = []
    null_names = ['Jacob', 'Stuart']
    letter_counter = 0      # If modulo %2==0 then index of hidden letter is 2 else 3
    for letter in message:
        if letter_counter % 2 == 0:
            index = 1
        else:
            index = 2
        for family in names_list:
            if family[index].lower() == letter.lower()\
            and family not in supporter_list and family not in null_names:
                supporter_list.append(family)
                letter_counter += 1
                break

    if len(supporter_list) < len(message):
        print("Word list is too small. Try larger dictionary or shorter message")
    else:
        for null_name in null_names:
            position = secrets.randbelow(len(supporter_list)- 4)
            supporter_list.insert(position, null_name.lower())

        while True:
            name_index = secrets.randbelow(len(supporter_list))
            if names_list[name_index] not in supporter_list:
                supporter_list.insert(0, names_list[name_index])
                break

    print("""Your Royal Highness: \n
It is with the greatest pleasure I present the list of noble families who
have undertaken to support your cause and petition the usurper for the
release of your Majesty from the current tragical circumstances.""")
    print( *supporter_list, sep="\n")

if __name__ == '__main__':
    main()
