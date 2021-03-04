def say_hello(first,last):
    print(f"{first} says hello to {last}")

names = {"first" : "Prithvi" , "last" : "Messi"}

#unpacking the dictionary
say_hello(**names)