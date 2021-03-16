# A key feature in OOP that allows us to define a class which inherits from another class.

class Animal:
    cool = True

    def make_sound(self,sound):
        print(f"Animal says {sound}")

class Cat(Animal):
    pass

kitty = Cat()
print(kitty.make_sound("Meow"))
print(kitty.cool)

print(isinstance(kitty,Cat)) #True
print(isinstance(kitty,Animal)) #True
