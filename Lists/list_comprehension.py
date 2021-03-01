# Manipulating the values in the List to give out a new list.

nums = [1,2,3,4,,6]
new_nums = [x * 10 for x in nums] # [10, 20, 30, 40, 50]

names = ["harry","ron","hermione"]
upper_case_names = [name.upper() for name in names] #['HARRY', 'RON', 'HERMIONE']
camel_case_names = [name[0].upper() + name[1:] for name in names] #['Harry', 'Ron', 'Hermione']

nums_to_string = [str(num) for num in nums] #['1', '2', '3', '4', '5']

check_if_truthy = [bool(val) for val in ("",[],0)] #[False, False, False]

