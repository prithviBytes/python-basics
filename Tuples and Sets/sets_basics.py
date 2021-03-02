# Collection of data that donot have duplicate values.
# Elements are unordered.
# Cannot access an item with index.

temp = {1,2,3,4,5}

temp = set({1,2,3,4,4,3,2,1,2,5})

4 in temp # returns True

for number in temp:
    print(number)

numbers = [1,2,3,3,3,4,4,4,5,5,5,6,6,6,7]

print(list(set(numbers))) # [1, 2, 3, 4, 5, 6, 7] removes duplicates

print(len(set(numbers))) # 7 returns the number of unique elements in the list

