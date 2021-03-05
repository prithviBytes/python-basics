# Takes a lambda which return boolean value and a iterable object.
# Iterates through the iterable and for each item executes the lambda.
# If the lambda for that particular item is true then it saves into the filter_object.

evens = filter(lambda x: x % 2 == 0,[1,2,3,4,5,6,7])

print(evens) # Returns a filter_object
print(list(evens)) # Return a list from evens