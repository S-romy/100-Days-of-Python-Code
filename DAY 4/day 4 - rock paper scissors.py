import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

# User input generation
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if user_input >= 0 and user_input <= 2:
    print(game_images[user_input])
else:
    print("Your input is invalid!")

# Computer input generation.
computer_input = random.randint(0, 2)
print(f"The computer chose: {game_images[computer_input]}")

# Game rules.
if user_input == 0 and computer_input == 0:
    print("It's a tie! Nobody wins!")
elif user_input == 1 and computer_input == 1:
    print("It's a tie! Nobody wins!")
elif user_input == 2 and computer_input == 2:
    print("It's a tie! Nobody wins!")
elif user_input == 0 and computer_input == 2:
    print("You win!")
elif user_input == 1 and computer_input == 0:
    print("You win!")
elif user_input == 2 and computer_input == 1:
    print("You win!")
elif user_input == 1 and computer_input == 2:
    print("The computer wins!")
elif user_input == 2 and computer_input == 0:
    print("The computer wins!")
elif user_input == 0 and computer_input == 1:
    print("The computer wins!")
else:
    print("Game Over!")
