def multiply_even_numbers(arr):
    total = 1
    for item in arr:
        if(item % 2 == 0):
            total = total * item
    return total

print(multiply_even_numbers([1,2,2,3,4,5,6]))