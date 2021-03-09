
try:
    num = int(input("Enter a number"))
except:
    print("Runs if some exception takes place")
else:
    print("If everything is fine will execute")
finally:
    print("THis runs no matter what.")
