from copy import copy

class Human:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def __repr__(self):
        return f"Hello! My name is {self.first_name} {self.last_name}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first_name="NewBorn",last_name=self.last_name,age=0)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, int):
            return [ copy(self) for i in range(other) ]
        else:
            raise TypeError

    def incrementAge(self):
        self.age += 1
        return self

j = Human("Leo","Messi",50)

k = Human("Anto","Roccu",49)

l = j + k

m = j * 3

# print(l) # Hello! My name is NewBorn Messi
# print(m) # [Hello! My name is Leo Messi, Hello! My name is Leo Messi, Hello! My name is Leo Messi]

m[0].incrementAge()

for human in m:
    print(human.age)