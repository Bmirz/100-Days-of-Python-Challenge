student_dict = {
    "student": ["Angela", "Bilal", "James", "Lily"],
    "score": [56, 99, 76, 98]
}

# # Looping through dictionaries
# for (key,value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# #Loop through a data frame
# for (key,value) in student_data_frame.items():
#     print(value)

#Loop through each row instead of each column
for (index,row) in student_data_frame.iterrows():
    print(row)

# for (index,row) in student_data_frame.iterrows():
#     if row.student == "Bilal":
#         print(row.score)