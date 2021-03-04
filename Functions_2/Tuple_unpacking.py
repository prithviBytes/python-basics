# Pack the arguments into tuple
def total(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

numbers = [1,2,3,4,5,6,7,9,10]

total(*numbers) #unpacks the list