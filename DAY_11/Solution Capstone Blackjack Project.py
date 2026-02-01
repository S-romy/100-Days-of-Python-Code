import random
import art


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a tie!"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif c_score == 0:
        return "You lose, Computer has a Blackjack!"
    elif u_score > 21:
        return "You went over so you lose!"
    elif c_score > 21:
        return "Computer went over so you win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "Computer wins!"


def game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_score > 21 or user_score == 0 or computer_score == 0:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    game()
