import pandas

data = pandas.read_csv("day026/NATOalphabetProject/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #My Solution
# phonetic_dict = {}
# #Loop through rows of a data frame
# for (index, row) in data.iterrows():
#     phonetic_dict.update({row.letter: row.code})
# # print(phonetic_dict)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Input word you would like phonetically spelled out: ").upper()

# #My Solution
# for char in user_input:
#     for (key, value) in phonetic_dict.items():
#         if key == char:
#             print(f"{value}")

output_list = [phonetic_dict[letter] for letter in user_input]
print(output_list)