from art import logo
import random

def get_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return (10)
    print("easy")
  elif difficulty == 'hard':
    return(5)
    print("easy")
  else:
    print("Invalid entry.")
    guess_number()


def guess_number():
  print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
  
  number = random.randint(1, 100)
  attempts = get_difficulty()
  
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
      print(f"You guessed it! The number is {number}.")
      attempts = 0
    elif guess > number:
      print("Too high...")
      attempts -= 1
    elif guess < number:
      print("Too low...")
      attempts -= 1
    else:
      print("invalid input")

  if guess != number:
    print(f"You lose! The number was {number}.")
  
print(logo)
guess_number()
