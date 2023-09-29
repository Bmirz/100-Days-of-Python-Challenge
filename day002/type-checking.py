num_char = len(input("What is your name?\n"))

# print("Your name has " + num_char + "characters.") - Error "num_char" is wrong type 

print(type(num_char))

new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.")
