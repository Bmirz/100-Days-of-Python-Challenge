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

# *** Proper Solution ***

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)
