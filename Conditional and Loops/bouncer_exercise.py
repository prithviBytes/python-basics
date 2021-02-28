age = input("How old are you? :")

if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You need to wear a wrist band...")
    elif age >= 21:
        print("Normal Entry. Have a good day...")
    else:
        print("Too young...Do your homework...")
else:
    print("Please enter a valid age...")