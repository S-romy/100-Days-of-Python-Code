import pandas

art = """
    _   _____  __________     ____  __  ______  _   ________________________   ___    __    ____  __  _____    ____  ____________
   / | / /   |/_  __/ __ \   / __ \/ / / / __ \/ | / / ____/_  __/  _/ ____/  /   |  / /   / __ \/ / / /   |  / __ )/ ____/_  __/
  /  |/ / /| | / / / / / /  / /_/ / /_/ / / / /  |/ / __/   / /  / // /      / /| | / /   / /_/ / /_/ / /| | / __  / __/   / /   
 / /|  / ___ |/ / / /_/ /  / ____/ __  / /_/ / /|  / /___  / / _/ // /___   / ___ |/ /___/ ____/ __  / ___ |/ /_/ / /___  / /    
/_/ |_/_/  |_/_/  \____/  /_/   /_/ /_/\____/_/ |_/_____/ /_/ /___/\____/  /_/  |_/_____/_/   /_/ /_/_/  |_/_____/_____/ /_/     
                                                                                                                                 
"""

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {A: "Alpha", B: "Bravo"}
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
loop = True
while loop:
    print(art)
    print("Type 'EXIT' to close the program.")
    user_input = input("Enter a word: ").upper()

    if user_input == "EXIT":
        loop = False
    else:
        phonetic_code_list = [alphabet_dict[letter] for letter in user_input if letter in alphabet_dict]
        print(phonetic_code_list)
