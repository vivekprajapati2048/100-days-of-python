# *args: many positional arguments - calling by position

def add(*args):
    print(args)
    # print(type(args))
    # print(args[0])

    sum = 0
    for i in args:
        sum += i
    return sum

print(add(10, 12, 2, 1, 1, 5))



# **kwargs: many keywoard arguments - calling by name

def calculate(n, **kwargs):
    print(kwargs)

    # for key, value in kwargs.items():
    #     print(key)
    # print(kwargs[key])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)



# creating class to understand how keyword arguments works
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make") # kw["make"]
        self.model = kw.get("model") # kw["model"]
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.color)



# quiz question
def all_aboard(a, *args, **kw):
    print(a, args, kw)

print(all_aboard(4, 7, 3, 0, x=10, y=64))