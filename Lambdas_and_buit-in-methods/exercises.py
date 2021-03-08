
def sum_even_numbers(*numbers):
    return sum(number if number % 2 == 0 else 0 for number in numbers)

def sum_floats(*numbers):
    return sum(number for number in numbers if isinstance(number,float))

print(sum_even_numbers(1,3))

def inter_leave(str1,str2):
    return "".join([t[0]+t[1] for t in zip(str1,str2)])

print(inter_leave("lzr","iad"))

def triple_and_filter(numbers):
    return [number * 3 for number in numbers if number % 4 == 0]

print(triple_and_filter([1,2,3,4,5,6,6,7,8]))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(names):
    return list(map(lambda name: "{} {}".format(name['first'],name['last']),names))

print(extract_full_name(names))
