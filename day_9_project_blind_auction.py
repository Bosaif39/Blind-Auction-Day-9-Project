import os

# Dictionary to store bidders and their bid amounts
bids = {}

def clear_screen():
    """
    Clears the console screen based on the operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bid_records):
    """
    Determines the highest bidder and prints the result.
    """
    max_bid = 0
    winner_name = ""
    for bidder_name, bid_amount in bid_records.items():
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner_name = bidder_name
    print(f"The winner is {winner_name} with a bid of ${max_bid}")

auction_open = True
# Main loop to collect bids from users
while auction_open:
    bidder_name = input("Enter your name: ")
    bid_amount = int(input("Enter your bid: $"))
    bids[bidder_name] = bid_amount
    more_bidders = input("Are there more bidders? (yes/no): ").lower()
    clear_screen()
    
    # Check if the user wants to end the bidding process
    if more_bidders == "no":
        auction_open = False
    print("=" * 10)

find_highest_bidder(bids)
