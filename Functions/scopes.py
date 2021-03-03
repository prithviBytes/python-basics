number = 10 
# This variable has a global scope. i.e it can be accessed anywhere.
# BUT, the catch is if we want to access global variables inside the function then,
# we need to spcify global keywork in front of the variable inside the function if we want to 
# mutate it.
# REASON: when mutating the variable inside a function, it looks for the variable in the local
#         scope.

def demo_fn():
    global number # telling the function that if we encounter number then look into global scope :)
    number2 = 20 # This variable wouldn't be accessible outside the function.
    print(number2)
    number += 10
    print(number)

demo_fn()   


def demo_fn_2():
    message = "Hello"
    def child_fn():
        nonlocal message # for nested functions the childrens should be made aware of the variable
        message += " Prithvi"
        print(message)
    child_fn()

demo_fn_2()