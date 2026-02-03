# Lesson 5: Print is your friend; Squash bugs with the print() statement

# Problem
# word_per_page = 0
# number_of_pages = int(input("How many pages does the book have?: "))
# word_per_page == int(input("What are the words per page?: "))
# total_words = number_of_pages * word_per_page
# print(f"The book has an average of {total_words} words.")

# Solution
number_of_pages = int(input("How many pages does the book have?: "))
word_per_page = int(input("What are the words per page?: "))
total_words = number_of_pages * word_per_page
print(f"Number of pages = {number_of_pages}")
print(f"Word per page = {word_per_page}")
print(f"The book has an average of {total_words} words.")
