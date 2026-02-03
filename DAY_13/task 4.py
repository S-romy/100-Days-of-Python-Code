# Lesson 4: Fix errors and watch out for red underlines.

# Problem - ValueError: invalid literal for int() with base 10 when letters are inputted
# and the print statement indentation.

# age = int(input("What is your age?: "))
# if age > 18:
# print(f"You can drive at age {age}")

# Solution
try:
    age = int(input("What is your age?: "))
except ValueError:
    print("You typed an invalid number. Please try again with a numerical figure such as 15.")

    age = int(input("What is your age?: "))

if age > 18:
    print(f"You can drive at age {age}")
