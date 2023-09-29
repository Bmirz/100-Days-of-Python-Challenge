# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

print(f"The names entered are {names}")

payer = random.randint(0, len(names))

print(f"{names[payer]} will be paying the meal today!")
