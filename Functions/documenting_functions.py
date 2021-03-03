from random import randint


def say_hello():
    """This is a simple function that prints Hello"""
    print("Hello World!!!")

print(say_hello.__doc__) #This is a simple function that prints Hello

print(randint.__doc__) #Return random integer in range [a, b], including both end points.