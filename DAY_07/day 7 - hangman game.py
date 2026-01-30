import random
import wordlist
from stages import hangman, logo

# TODO 1: Update the word list to use the 'word_list' from wordlist.py

chosen_word = random.choice(wordlist.word_list)

# TODO 3: Import the logo from stages.py and print it at the start of the game.

print(logo)

lives = 6

placeholder = ""
length_of_word = len(chosen_word)
for word in range(length_of_word):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False

correct_letters = []

while not game_over:

    # TODO 6: Update the code below to tell the user how many lives they have left.

    print(f"*******************<???> {lives} LIVES LEFT <???>********************")

    guess = input("There is a random word! Can you guess one of the letters?: ").lower()

    # TODO 4: If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in correct_letters:
        print(f"You have already guessed the letter {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO 5: If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. you guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        print(f"The letter {guess} is not in chosen word.")

    if "_" not in display:
        game_over = True
        print("********************* YOU WIN! ********************")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True

            # TODO 7: Update the print statement below to give the user the correct word they were trying to guess.
            print(f"******************** THE WORD WAS {chosen_word}. YOU LOSE! *********************")

    # TODO 2: Update the code below to use the hangman list from the file stages.py
    print(hangman[lives])
