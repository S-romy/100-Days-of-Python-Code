from art import logo
print(logo)

print("Welcome to the Secret Auction")


def highest_bidder(bid_dict):
    winner = ""
    highest_amount = 0

    for bidder in bid_dict:
        bid_amount = bid_dict[bidder]

        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_amount}!")


bidding_dictionary = {}

other_bidders = True
while other_bidders:
    name = input("What is your name?: ")
    amount = int(input("What is the amount you want to bid?: $"))
    bidding_dictionary[name] = amount
    bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if bidders == "yes":
        print("\n" * 50)
    elif bidders == "no":
        other_bidders = False
        highest_bidder(bidding_dictionary)
