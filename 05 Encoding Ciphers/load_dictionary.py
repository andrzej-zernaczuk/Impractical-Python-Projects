"""load a text file as a list"""
import sys

def load(file):
    """Open a text file & return a list of lowercase strings"""

    try:
        with open(file, encoding="utf-8") as in_file:
            loaded_txt=in_file.read().strip().split('\n')
            loaded_txt=[x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as error:
        print(f"{error}\nError opening {file}. Terminating program.", file=sys.stderr)
        sys.exit(1)
