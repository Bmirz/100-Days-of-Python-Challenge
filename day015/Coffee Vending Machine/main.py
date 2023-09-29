
#-------IMPORTS-------
import sys
from coffee_data import MENU,resources

#-------GLOBAL VARIABLES-------
profit = 0
#-------FUNCTIONS-------
def coffee_input_validation():
  '''prompts user input and checks that user has only inputed character values'''
  #prompt
  user_input = input("What would you like? (espresso,latte,cappuccino): ").lower()
  #input validation
  while user_input.isalpha() == False and (user_input != 'espresso' or user_input != 'latte' or user_input != 'cappuccino'):
    user_input = input("Please input a valid request: ")
  return user_input

def coin_input_validation(coin_name):
  '''prompts user input coins and checks that user has only inputed integer values'''
  #prompt
  coin_input = input(f"how many {coin_name}?: ")#input validation
  while coin_input.isdigit() == False:
    coin_input = input(f"Please input a valid amount of {coin_name}: ")
  return int(coin_input)

def check_resources(user_input):
    '''checks that coffee machine has sufficient resources for a selected recipe'''
    selected_recipe = MENU.get(user_input)

    # Compare recipe requirements to coffee machine's current resources
    for ingredient, required_amount in selected_recipe['ingredients'].items():
        if required_amount > resources.get(ingredient):
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True

def update_resources(user_input):
   '''deducts resource cost of selected recipe from coffee machine resources'''
   selected_recipe = MENU.get(user_input)
   for ingredient, required_amount in selected_recipe['ingredients'].items():
      resources[ingredient] -= required_amount


def process_payment():
    '''prompts user to insert ellotted coins, deducts cost, and returns change.'''
    print("Please insert coins.")
    purse = 0
    purse += (coin_input_validation("quarters") * .25)
    purse += (coin_input_validation("dimes") * .10)
    purse += (coin_input_validation("nickles") * .05)
    purse += (coin_input_validation("pennies") * .01)
    print(f"${purse} inserted")
    return purse

while True:
    user_input = coffee_input_validation()

    if user_input == "off":
        print("Shutting down...💤")
        sys.exit()
    elif user_input == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")
        print(f"profit: {profit}")
    elif check_resources(user_input):
        print(f"Your {user_input} will cost ${MENU[user_input].get('cost')}")
        purse = process_payment()
        if purse < MENU[user_input].get('cost'):
            print("Insufficient funds...\nMoney refunded💰")
        else:
            profit += MENU[user_input].get('cost')
            purse -= MENU[user_input].get('cost')
            print(f"${purse} has been refunded")
            update_resources(user_input)
            print(f"Here is your {user_input}☕️. Enjoy!")
