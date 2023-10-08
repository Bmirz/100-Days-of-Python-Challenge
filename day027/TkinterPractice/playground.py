#Oct. 7, 2023

# # Traditional way of adding
# def add(a, b):
#     return a + b

# print(add(4,4))

# # Adding with unlimited args
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(5,3,7,1,9,4))

# # Writing a method that uses keywords
# def calculate(n, **kwargs):
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=5)

# How default values work
# Using .get()is preferred because if a keyword is not defined while intitilizing an object
# it will just return as none (as opposed to using [])
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)


