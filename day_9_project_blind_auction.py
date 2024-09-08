import os

#Dictionary to store bidders and their bid amounts
bidders = {}

def clear_screen():
    """
    Clears the console screen based on the operating system.
    
    Uses 'cls' command for Windows and 'clear' command for Unix-based systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def highest_bidder(bid_record):
    """
    Determines the highest bidder and prints the result.
    
    Parameters:
    bid_record (dict): A dictionary where keys are bidder names and values are their bid amounts.
    
    Prints:
    - The name of the highest bidder.
    - The amount of the highest bid.
    """
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bid_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the bid is ${highest_bid}")

Doer = True
#Main loop to collect bids from users
while Doer:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bidders[name] = price
    test = input("Are there more bidders? (yes/no): ").lower()
    clear_screen()
    
    #Check if the user wants to end the bidding process
    if test == "no":
        Doer = False
    elif test == "yes":
        print("=" * 10)

highest_bidder(bidders)
