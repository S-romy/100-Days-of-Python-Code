# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("/Users/Roseeeeeee/Udemy/DAY_24 II/Input/Names/invited_names.txt") as invited_names:
    replacements = invited_names.readlines()

with open("/Users/Roseeeeeee/Udemy/DAY_24 II/Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    word = content.split()[1]

    for replacement in replacements:
        stripped_replacement = replacement.strip()
        new_letter = content.replace(word, stripped_replacement + ",")

        with open(f"/Users/Roseeeeeee/Udemy/DAY_24 II/Output/ReadyToSend/"
                  f"letter_for_{stripped_replacement}.txt", mode="w") as output:
            output.write(new_letter)

    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
