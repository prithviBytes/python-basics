# Whenever you create a class, Python sets a Method Resolution Order,
# for that class, which is the order in which python will look out for methods
# on instances on that class.

class Aquatic:

    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"Hi I am {self.name} from the sea!!!"


class Ambulatory:

    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking!!!"

    def greet(self):
        return f"Hi I am {self.name} from the land"


class Penguin(Ambulatory, Aquatic):

    def __init__(self, name):
        super().__init__(name=name)


print(Penguin.__mro__)
print(Penguin.mro())
print(help(Penguin))

#  |  Method resolution order:
#  |      Penguin
#  |      Ambulatory