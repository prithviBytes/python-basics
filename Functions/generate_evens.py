

def generate_evens():
    evens = []
    for number in range(1,50):
        if number % 2 == 0:
            evens.append(number)
    return evens

print(generate_evens())

def generate_evens_with_comprehensions():
    return [number for number in range(1,50) if number % 2 == 0]

print(generate_evens_with_comprehensions())