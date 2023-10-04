#new_list = [new_item for item in list]

numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Bilal"
new_list = [letter for letter in name]
print(new_list)

range_list = [n * 2 for n in range(1,5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)