import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to the PyPassword Generator!")

no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))

password = []

# Generate random letter(s) using the user input
for letter in range(no_of_letters):
    l_password = random.choice(letters)
    password.append(l_password)

# Generate random symbol(s) using the user input
for symbol in range(no_of_symbols):
    s_password = random.choice(symbols)
    password.append(s_password)

# Generate random number(s) using the user input
for number in range(no_of_numbers):
    n_password = random.choice(numbers)
    password.append(n_password)

# Shuffle the password
random.shuffle(password)

# Convert password from list to string
shuffled_password = ''.join(password)
print(f"Your password is {shuffled_password}")
