def divide(num1,num2):
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("Donot try to divide by zero.")
    except TypeError as err:
        print("both should be a number")
        print(err)
    else:
        return result

print(divide(36,3))
print(divide("a",2))
print(divide(1,0))