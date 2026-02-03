# Lesson 3: Play Computer.

# Problem
# year = int(input("What is your year of birth?: "))
#
# if year > 1980 and year < 1994:
#     print("You're a Millennial")
# elif year > 1994:
#     print("You're a Gen Z")

# Solution
year = int(input("What is your year of birth?: "))

if year > 1980 and year <= 1994:
    print("You're a Millennial")
elif year > 1994:
    print("You're a Gen Z")
