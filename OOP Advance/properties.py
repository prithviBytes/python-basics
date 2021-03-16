
class Human:

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        if age >= 0:
            self._age = age
        else:
            self._age = 0
    
    # def get_age(self):
    #     return self._age

    # def set_age(self,new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property #makes the method as a property of the object.
    def age(self):
        return self._age

    @age.setter # can assign value directly to te setter
    def age(self,new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age cannot be negative")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self,full_name):
        self.first_name, self.last_name = full_name.split(" ")
messi = Human("Lionel","Messi",34)

print(messi.age)
messi.age = 25
print(messi.age)
print(messi.full_name)
messi.full_name = "Cristiano Ronaldo"
print(messi.full_name)
print(messi.__dict__)