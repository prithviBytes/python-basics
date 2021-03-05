# A standard functions that accepts atleast 2 arguments.
#   1. An iterable.
#   2. A function.

# Iterates and executes the function to each and every item.
# Returns a map object.
nums = [1,2,3,4,5,6]
doubles = map(lambda x: x * 2,nums)

print(doubles) # <map object at 0x000002020789BFA0>

for number in doubles:
    print(number)

print(list(doubles)) #[2, 4, 6, 8, 10, 12]
print(list(doubles)) #[]

# Note: THe map object can be iterated or converted to another data type only ONCE.
