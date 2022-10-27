"""Generate funny names by randomly combining names from 2 separate lists."""
import sys
import random

def main():
    """Generate funny names by randomly combining names from 2 separate lists."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first_old=('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
    "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
    'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
    'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
    'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
    'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
    'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
    'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
    'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
    'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
    'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
    "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
    'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
    'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
    "Winston 'Jazz Hands'", 'Worms')

    last=('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
    'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
    'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
    'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
    'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
    'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
    'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
    'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
    'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
    'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
    'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
    'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
    'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
    'Woolysocks')

    first_to_tuple=[]
    middle_to_tuple=[]

    for name in first_old:
        if " '" in name:
            names_to_split=[]
            names_to_split=name.split(maxsplit=1)
            first_to_tuple.append(names_to_split[0])
            middle_to_tuple.append(names_to_split[1][1:-1])
        else:
            first_to_tuple.append(name)

    first=tuple(first_to_tuple)
    middle=tuple(middle_to_tuple)

    print(first)
    print(middle)

    while True:
        first_name=random.choice(first)
        middle_name=random.choice(middle)
        last_name=random.choice(last)
        print("\n")
        if random.randrange(1,4)%2==0:
            print(f"{first_name} {middle_name} {last_name}")
        else:
            print(f"{first_name} {last_name}")
        print("\n")
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
        if try_again.lower()=="n":
            sys.exit()

    input("\nPress Enter to exit.")

if __name__=="__main__":
    main()
    