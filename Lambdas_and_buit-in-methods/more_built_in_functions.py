# all: checks if all items in a iterable is truthy
names = ["Crist","Charlie","Cassindra"]
all([name[0] == "C" for name in names]) #True
names.append("Tom")
all([name[0] == "C" for name in names]) #False

#any: checks if any of the items are truthy
any([name[0] == "T" for name in names]) #True

#sort: doesn't sort the exisiting iterable but returns a copy of sorted iterable.
numbers = [3,2,6,4,1,6,7,9]
print(sorted(numbers)) #[1, 2, 3, 4, 6, 6, 7, 9]
print(sorted(numbers,reverse=True)) # [9, 7, 6, 6, 4, 3, 2, 1]
print(numbers) # [3, 2, 6, 4, 1, 6, 7, 9]

names = ["Crist","Charlie","Cassindra","Tim","Messi"]

#max: returns the max in the iterable
max(numbers) #9
max(names,key = lambda x:len(x)) # Cassinndra
#min: returns min from a iterable
min(numbers) #1
min(names,key = lambda x:len(x)) # Tim


# reversed: returns a iterable object with the contents reversed.
"".join(list(reversed("Prithvi"))) #ivhtirP

#abs: returns the magnitude of the number irrespective of its sign
abs(5) #5
abs(-5) #5

# sums: adds all the number in an iterable and returns the sum. OPTIONALLY you can specify the start value
sum([1,2,3],10) #16

# round: rounds the number to a decimal precision. If 2nd argument is not passed then,
# It would be rounded off to an Integer.
round(3.2222) #3
round(3.2222,2) #3.22

# zip: zips an iterable together
number1 = [1,2,3,4,5]
number2 = ["first","second","third","forth","fifth"]
zipped = zip(number1,number2)
zipped_numbers = dict(zipped) #{1: 'first', 2: 'second', 3: 'third', 4: 'forth', 5: 'fifth'}

