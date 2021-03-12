class BankAccount:
    
    active_users = 0 # attribute is specific to the class and has nothing to do with the instances
 
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
        BankAccount.active_users += 1
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        return self.balance

user1 = BankAccount("Prithvi")
user2 = BankAccount("Lionel")

print(BankAccount.active_users)


class Pet:
    
    allowed_species = ["cat","dog"]

    def __init__(self,name,species):
        if species not in Pet.allowed_species:
            raise ValueError(f"You cannot have {species} as a pet")
        self.name = name
        self.species = species
        print(f"Congrats on having {self.name}, a {self.species} as your pet!!!")