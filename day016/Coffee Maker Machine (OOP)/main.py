import sys
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

#1 - Print Reports
# coffee_maker.report()
# money_machine.report()

#2 - Check resources are sufficient
while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == 'off':
        print("Shutting down...💤")
        sys.exit()
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        #3 - Process coins/ #4 - Check transaction is successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                #5 - Make Coffee
                coffee_maker.make_coffee(drink)


# while True:
#     user_input = input("What would you like?")
#     print(Menu.get_items())

    # if user_input == "off":
    #     print("Shutting down...💤")
    #     sys.exit()
    # elif user_input == "report":
    #     for key, value in resources.items():
    #         print(f"{key}: {value}")
    #     print(f"profit: {profit}")
    # elif check_resources(user_input):
    #     print(f"Your {user_input} will cost ${MENU[user_input].get('cost')}")
    #     purse = process_payment()
    #     if purse < MENU[user_input].get('cost'):
    #         print("Insufficient funds...\nMoney refunded💰")
    #     else:
    #         profit += MENU[user_input].get('cost')
    #         purse -= MENU[user_input].get('cost')
    #         print(f"${purse} has been refunded")
    #         update_resources(user_input)
    #         print(f"Here is your {user_input}☕️. Enjoy!")
