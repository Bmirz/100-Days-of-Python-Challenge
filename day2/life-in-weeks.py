# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

time_left = 90 - int(age)

days = time_left * 365
weeks = time_left * 52
months = time_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
