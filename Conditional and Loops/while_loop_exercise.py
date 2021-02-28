password = input("What is the secret password? \n")

while password != "bananas":
    password = input("Wrong Password! \n Try again: ")

print("Great! You may proceed...")


num = 1
while num <= 10:
    print(num)
    num += 1