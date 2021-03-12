class User:

    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self,thing):
        return f"{self.first} likes {thing}"

user1 = User("Prithvi","Suvarna")

print(user1.full_name())
print(user1.initials())
print(user1.likes("Vada Pav"))
    
