# Lesson 1: Describe the problem.
# Problem


def function():
    for i in range(1, 20):
        if i == 20:
            print("Okay!")


function()

# Describe the problem - Write your answers as comments:
# 1. What is the for loop doing?
# Ans: The loop runs from 1 to 19, it doesn't get to 20.
# 2. When is it meant to print "Okay!"?
# Ans: When it gets to 20.
# 3. What are your assumptions about the value of i?
# Ans: The value of i runs from 1 and stops at 19.


# Solution
def function():
    for i in range(1, 21):
        if i == 20:
            print("Okay!")


function()
