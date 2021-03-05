# Anonymous functions.
# These are not named.
# Functionality similar to functions.

## EXAMPLES

square = lambda num: num * num
print(square(10)) # 100

add = lambda a,b: a + b
print(add(1,2)) # 3

print(square.__name__) # returns lambda cause they don't have a name.