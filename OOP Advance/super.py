# Inside a children class super acts like a reference to the parent.


class Animal:

    def __init__(self,name,species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self,sound):
        return f"{self.name} says {sound}"

class Cat(Animal):

    def __init__(self,name,breed,toy):
        # Animal.__init__(self,name,species)
        super().__init__(name,species = "Cat")
        self.breed = breed
        self.toy = toy
    
    def plays(self):
        return f"{self.name} plays with {self.toy}"

kitty = Cat("kitto","persian","couch")

print(kitty.breed)
print(kitty.plays())