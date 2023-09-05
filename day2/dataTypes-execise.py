# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(type(two_digit_number))

int(two_digit_number)

second_digit = int(two_digit_number) % 10
first_digit = (int(two_digit_number) - second_digit) / 10

print(first_digit + second_digit)
