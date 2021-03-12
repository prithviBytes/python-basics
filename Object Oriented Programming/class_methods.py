class BankAccount:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"Current Active Users = {cls.active_users}"

    @classmethod
    def from_string(cls,str):
        first,last,age = str.split(',')
        cls(first,last,age)

 
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.balance = 0.0
        BankAccount.active_users += 1
        print(f"Account Created: {self.first} {self.last} {self.age}")
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        return self.balance

print(BankAccount.display_active_users())
user1 = BankAccount.from_string("Prithvi,Suvarna,22")
print(BankAccount.display_active_users())
user2 = BankAccount("Lionel","Ronaldo","34")
print(BankAccount.display_active_users())