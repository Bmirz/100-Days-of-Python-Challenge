rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choice = input("Welcome to rock, paper, scissors simulator! Whats your move? \n(Type 0 for Rock, 1 for Paper, or 2 for Scissors)\n")

if player_choice == "0":
  player_choice = rock
elif player_choice == "1":
  player_choice = paper
elif player_choice == "2":
  player_choice = scissors
else:
  input("Please input a valid option \nWhat do you choose? (Type 0 for Rock, 1 for Paper, or 2 for Scissors)\n")

computer_choice = random.randint(0,2)

if computer_choice == 0:
  computer_choice = rock
elif computer_choice == 1:
  computer_choice = paper
else:
  computer_choice = scissors

print(player_choice)
print("Computer chose:")
print(computer_choice)

if player_choice == computer_choice:
  print("Its a Draw!")
elif (player_choice == rock and computer_choice == scissors) or (player_choice == paper and computer_choice == rock) or (player_choice == scissors and computer_choice == paper):
  print("You Win!")
else:
  print("You Lose!")
