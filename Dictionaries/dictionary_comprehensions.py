numbers = dict(first = 1 , second = 2 , thrid = 3)

squared_numbers = { key : value ** 2 for key,value in numbers.items() } #returns squared values

squared_numbers_from_a_list = { number : number ** 2 for number in [1,2,3,4,5] }

str_one = "ABCDEFG"
str__two = "1234567"

combo = { str_one[i] : str__two[i] for i in range(0,len(str_one)) }

person_one = {
    "name" : "prithvi",
    "gender" : "male"
}

uppercase_person_one = { k.upper() : v.upper() for k,v in person_one.items() }

numbers = [1,2,3,4,5,6,7,8,9]

odd_or_even = { number : "even" if number % 2 == 0 else "odd" for number in numbers}

