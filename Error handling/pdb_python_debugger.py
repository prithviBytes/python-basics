import pdb

first = "first"
second = 'second'
pdb.set_trace()
result = first + second
third = 'third'
result += third
print(result)

# l => shows where we are
# n => next line
# c => continue