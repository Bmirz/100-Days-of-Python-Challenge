from replit import clear

from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secrete auction program!")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  top_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > top_bid:
      top_bid = bid_amount
      winner = bidder
  print(f"The winner of the auction is {winner} with the heighest bid of {top_bid}")

while bidding_finished is False:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_bidders == 'no':
    bidding_finished = True
    find_highest_bidder(bids)
  elif other_bidders == 'yes':
    clear()
