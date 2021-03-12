class BankAccount:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"Current Active Users = {cls.active_users}"
 
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

print(BankAccount.display_active_users())
account1 = BankAccount("Prithvi")
print(BankAccount.display_active_users())
account2 = BankAccount("Lionel")
print(BankAccount.display_active_users())