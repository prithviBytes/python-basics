numbers = {1,2,3,4,5,6}

# ADD: adding an item to the set.
numbers.add(7) # {1, 2, 3, 4, 5, 6, 7}

# REMOVE: removing an elemt from the set but throws an error if it doesnt exist
numbers.remove(7) # {1, 2, 3, 4, 5, 6}

# DISCARD: Same as remove but doesnt throw an error.
numbers.discard(7)

#COPY: copies the set to new variable in different memory
numbers_copy = numbers.copy()

# CLEAR: clears the entire set
numbers_copy.clear() # set()



