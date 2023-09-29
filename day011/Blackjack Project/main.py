import random
from replit import clear
from art import logo

def deal_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if len(cards) == 2 and sum(cards) == 21:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, dealer_score):
  if user_score == dealer_score:
    return "Draw 🙃"
  elif dealer_score == 0:
    return "Lose, opponent has Blackjack! 😓"
  elif user_score == 0:
    return "Won with a Blackjack! 🤩"
  elif user_score > 21:
    return "Bust! You lose 😣"
  elif dealer_score > 21:
    return "Dealer Busted. You win! 🥳"
  elif user_score > dealer_score:
    return "You win! 😁"
  else:
    return "You lose. 😓"

def play_game():
  user_cards = []
  dealer_cards = []
  
  game_over = False
  
  print(logo)
  
  for _ in range(2):
    user_cards.append(deal_cards())
    dealer_cards.append(deal_cards())
  
  while not game_over:
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Dealers first card: [{dealer_cards[0]}]")
    
    if user_score == 0 or dealer_score == 0 or user_score > 21:
      game_over = True
    else:
      user_deal = input("Type 'y' to get another card, or type 'n' to pass: ")
      if user_deal == 'y':
        user_cards.append(deal_cards())
      else:
        game_over = True
  
  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_cards())
    dealer_score = calculate_score(dealer_cards)
  
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Dealer's Final hand: {dealer_cards}, final score: {dealer_score}")
  print(compare(user_score, dealer_score))
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  play_game()
