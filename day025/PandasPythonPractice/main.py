# # How we know to utilize file data from previous practice with txt files
# with open("day025/weather_data.csv", 'r') as data_file:
#     data = data_file.readlines()
#     print(data)

# # utilizing pythons built in CSV import
# import csv

# with open("day025/weather_data.csv", 'r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# # utilizing py.data's Pandas import to manipulate data
# import pandas

# data = pandas.read_csv("weather_data.csv")

# # Shows how panda reorganizes CSV data: Entirity of fil is called "data frame", a column would be refered to as a "series"
# print(type(data))
# print(type(data["temp"]))
# print(data["temp"])

# # Turns CSV file data into a dictionary using pandas method '.to_dict()'
# data_dict = data.to_dict()
# print(data_dict)

# # Turning data in a series into a list using 'to_list()'
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# # Finding the average traditional versus panda methods
# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data["temp"].mean())

# # Challenge: Find the max value in Temperatue series
# print(data["temp"].max())

# # Get data in columns - both virtually the same
# print(data["condition"])
# print(data.condition)

# # Get data in row
# print(data[data.day == "Monday"])

# # Challenge: Locate the row in which the temp was at the highest
# print(data[data.temp == data.temp.max()])

# # Assigning a row to a variable
# monday = data[data.day == "Monday"]
# print(monday.condition)

# # Challenge: Convert monday's temperature into fahrenheit
# temp_fahrenheit = monday.temp * 1.8 + 32
# print(temp_fahrenheit)

# # Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv") #creates a csv in the current directory