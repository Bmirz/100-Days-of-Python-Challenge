#-------IMPORTS-------
import random
from replit import clear
from art import logo
from game_data import data

#-------GLOBAL_VARIABLES-------
score = 0
game_over = False

#-------FUNCTIONS-------
#function 'get_choice' returns user input after porper validation
def get_choice():
  #take input for user choice and convert to uppercase lettering always
  choice = input("\nWho has more followers? Type 'A' or 'B': ").upper()
  #input validation
  while choice != 'A' and choice != 'B':
    choice = input("Please input a valid option: ")
  return choice

#function 'get_answer' returns the correct choice out of the two options
def get_answer():
  if int(optionA['follower_count']) > int(optionB['follower_count']):
    answer = 'A' 
  else:
    answer = 'B'
  return answer


#initial logo print
print(logo)
while game_over == False:
  #assign random choice from game_data to options A and B
  optionA = random.choice(data)
  optionB = random.choice(data)
  
  #ensures there is no comparing of the same two options
  while optionB == optionA:
    optionB = random.choice(data)
  
  #print option 'A'
  print(f"Compare 'A': {optionA['name']}, the {optionA['description']}, from {optionA['country']}")
  
  #print vs.
  from art import vs
  print(vs)
  
  #print option 'B'
  print(f"Against 'B': {optionB['name']}, the {optionB['description']}, from {optionB['country']}")
  
  user_choice = get_choice()
  answer = get_answer()
  
  if answer == 'A' and user_choice == 'A':
    score += 1
    clear()
    print(logo)
    print(f"You're right! Current score: {score}.")
  elif answer == 'B' and user_choice == 'B':
    score += 1
    clear()
    print(logo)
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    game_over = True
