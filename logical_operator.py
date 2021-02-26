print("What is your age?")
age = int(input())
message = "You are a"

if age < 1:
    print(f"{message} baby")
elif age >= 1 and age <=3:
    print(f"{message} toddler")
elif age >= 4 and age <= 12:
    print(f"{message} Child")
elif age >= 13 and age <= 19:
    print(f"{message} teen")
else:
    print("You are an adult...")