"""Input cipher key string, get user input on route direction as dict value."""
COL_ORDER = """1 3 4 2"""

decryption_key = dict()
cols = [int(i) for i in COL_ORDER.split()]
for col in cols:
    while True:
        decryption_key[col] = input(f"Direction to read column {str(col).lower()} u = up, d = down): ")
        if decryption_key[col] == 'u' or decryption_key[col] == 'd':
            break
        else:
            print("Input should be either 'u' or 'd'")

print(decryption_key)
