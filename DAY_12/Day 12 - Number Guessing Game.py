import random
from art import logo

lives = 0


def generate_num():
    """Function to generate a random number"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
               41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
               61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
               81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    number = random.choice(numbers)
    return number


def difficulty(choice):
    """Function that sets the game lives according to the difficulty level"""
    global lives
    if choice == "easy":
        lives = 10
    elif choice == "hard":
        lives = 5
    else:
        return "Error! You typed a wrong input. Game Over!"

    return f"You have {lives} attempts remaining to guess the number."


def number_game():
    """The function that compares the player's guesses with the
     generated number and also keeps track of the player's lives"""
    global lives
    rand_num = generate_num()

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print(difficulty(level))

    game_over = False
    while not game_over:
        if level == "easy" or level == "hard":
            guess = int(input("Make a guess: "))
            if guess != rand_num and lives == 1:
                print(f"You are out of guesses. You lose! The number was {rand_num}.")
                game_over = True
            elif guess == rand_num:
                print(f"You got it right! The number was {rand_num}")
                game_over = True
            elif guess > rand_num and lives != 1:
                lives -= 1
                print("Too high!")
                print("Guess again.")
                print(f"You have {lives} attempts remaining to guess the number.")
                game_over = False
            elif guess < rand_num and lives != 1:
                lives -= 1
                print("Too low!")
                print("Guess again.")
                print(f"You have {lives} attempts remaining to guess the number.")
                game_over = False
        else:
            game_over = False


number_game()
