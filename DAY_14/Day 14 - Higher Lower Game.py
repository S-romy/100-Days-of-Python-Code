import random
from data import dataset
from logo import art, vs


def generate_dataset():
    """Generate data for the game"""
    random_data = random.choice(dataset)
    return random_data


def modify_dataset(datum):
    """Modify the data generated to suit the game"""
    account_name = datum["name"]
    account_description = datum["description"]
    account_country = datum["country"]
    return f"{account_name}, a {account_description}, from {account_country}."


def game_rules(account_a, account_b, follower_a, follower_b):
    """Outlines the rules the game should follow where the user with more followers becomes the input for A."""
    if follower_a == follower_b:
        return account_a
    elif follower_a > follower_b:
        return account_a
    elif follower_b > follower_a:
        return account_b


def game():
    """The game function and how it operates"""
    score = 0

    print(art)

    # Generate the value for A.
    a = generate_dataset()
    compare_a = modify_dataset(a)
    a_followers = a["follower_count"]
    print(f"Compare A: {compare_a}")

    print(vs)

    # Generate the value for B.
    b = generate_dataset()
    while a["follower_count"] == b["follower_count"]:
        b = generate_dataset()
    against_b = modify_dataset(b)
    b_followers = b["follower_count"]
    print(f"Against b: {against_b}")

    # The game should keep going till the user's guess is wrong.
    game_over = False
    while not game_over:
        # The user input for the game
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Comparing the value of A with the value of B to generate the next value.
        if user_guess == "A" and a_followers > b_followers or user_guess == "B" and b_followers > a_followers:
            game_over = False
            print("\n"*20)
            print(art)

            # Keeping count on score.
            score += 1
            # Giving the user feedback when their guess is right.
            print(f"You're right! Current score = {score}")

            # The next value of A depends on the game_rules function.
            a = game_rules(a, b, a_followers, b_followers)
            compare_a = modify_dataset(a)
            a_followers = a["follower_count"]
            print(f"Compare A: {compare_a}")

            print(vs)

            # Generate a new value for B.
            b = generate_dataset()
            while a["follower_count"] == b["follower_count"]:
                b = generate_dataset()
            against_b = modify_dataset(b)
            b_followers = b["follower_count"]
            print(f"Against b: {against_b}")

        else:
            game_over = True
            print("\n"*20)
            print(art)
            # Giving the user feedback when their guess is wrong.
            print(f"Sorry! That's wrong. Final score = {score}")


game()
