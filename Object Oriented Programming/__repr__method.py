class User:

    def __repr__(self):
        return f"{self.first} {self.last} is {self.age} years old."

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

user1 = User("Prithvi","Suvarna",22)

print(user1) #Before adding __repr__ method prints <__main__.User object at 0x000002084F96BFD0>

print(user1) # Prithvi Suvarna is 22 years old. after adding __repr__method.

# __repr__ stands for representation.
