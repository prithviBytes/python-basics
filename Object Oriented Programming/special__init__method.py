# __init__ is a special method in class which acts like a constructor to
# initialize values.


class User:

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age =age

user1 = User("Prithvi","Suvarna",22)
user2 = User("Lionel","Messi",34)

print(user1.first,user1.last,user1.age)
print(user2.first,user2.last,user2.age)