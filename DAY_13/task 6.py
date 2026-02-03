import random
import maths

# Lesson 6: Use a debugger - The big gun


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)

    # Problem: b_list.append(new_item) was not indented into the loop, so it appended the last number only to the list.
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
