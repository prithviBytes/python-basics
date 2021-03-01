person_one = {
    "name" : "Prithvi",
    "age" : 22,
    "gender" : "Male"
}

person_two = dict(name = "Lionel", age = "34", gender = "Male") #{'name': 'Lionel', 'age': '34', 'gender': 'Male'}


# Accessing the values. If the key doesnt exist then it will throw an error.
person_one["name"] # Prithvi

# Accessing all the values via VALUES
for value in person_one.values():
    print(value)

# Accessing all the values via KEY
for key in person_one.keys():
    print(key)

# Accessing all the key and values
for key,value in person_one.items():
    print(f"{key}: {value}")

# Verifying if a key is in a dictionary.
"name" in person_one #True
"breed" in person_one #False

# Verifying if a value is in the dictionary
"Prithvi" in person_one.values() #True
"Ronaldo" in person_one.values() #False


