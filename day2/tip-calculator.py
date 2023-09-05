#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

bill = float(input("what was the total bill? "))

percentage = int(input("What percentage of tip would you like to give? "))/100

split = int(input("How many people are spliting the bill? "))

print(f"{bill} {percentage} {split}")

payment = round(int(bill) + (int(bill) * float(percentage)) / int(split), 2)

print(f"Each person should pay: {payment}")
