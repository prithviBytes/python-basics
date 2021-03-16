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


fish = Aquatic("Nimo")
cat = Ambulatory("Kitty")
captain_cook = Penguin("cook")

print(captain_cook.walk())
print(captain_cook.swim())
print(captain_cook.greet()) #Hi I am cook from the land
