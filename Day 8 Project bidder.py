import os
bidders = {}
Doer = True

#Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#Function to find the highest bidder
def highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the bid is ${highest_bid}")

#Loop to take as much bidders as needed
while Doer:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bidders[name] = price
    test = input("Are there more bidders? (yes/no): ").lower()
    clear_screen()
    if test == "no":
        Doer = False
    elif test == "yes":
        print("=" * 10)

highest_bidder(bidders)
