FILENAME = "hopsen5.txt"
# Open and read file
with open(FILENAME, "r") as f:
    lines = f.read()

# Filter alphabetic characters, including German-specific letters
stripped_text = "".join(
    [i.lower() for i in lines if i.isalpha() or i.lower() in "äöüß"]
)

end = len(stripped_text)


# Character-to-integer conversion including German letters
def ctoi(char):
    if char == "ä":
        return 27
    elif char == "ö":
        return 28
    elif char == "ü":
        return 29
    elif char == "ß":
        return 30
    val = ord(char) - 96
    return val  # Handles normal letters a-z


# Initialize positions for Bela and Amira
bela_pos = 0  # Bela starts at index 0
amira_pos = 1  # Amira starts at index 1
bela_moves = 0
amira_moves = 0

# Ensure there is enough length for Amira to start
if len(stripped_text) <= 1:
    print("Text too short for game.")
else:
    while True:
        # Bela's move
        bela_pos += ctoi(stripped_text[bela_pos])
        bela_moves += 1
        if bela_pos >= len(stripped_text):  # Check if Bela won
            print("Bela won!")
            break

        amira_pos += ctoi(stripped_text[amira_pos])
        amira_moves += 1
        if amira_pos >= len(stripped_text):  # Check if Amira won
            print("Amira won!")
            break
    print("Amira:\t", amira_moves, "moves")
    print("Bela:\t", bela_moves, "moves")
