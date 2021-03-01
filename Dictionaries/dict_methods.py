person_one = {
    "name" : "Prithvi",
    "age" : 22,
    "gender" : "Male",
    "hobbies" : "Football",
    "language" : "javscript"
}

# CLEAR to clear the dictionary
person_one.clear() # {}

person_one = {
    "name" : "Prithvi",
    "age" : 22,
    "gender" : "Male",
    "hobbies" : "Football",
    "language" : "javscript"
}

#COPY creates a copy of the dictionary, but it doesnt refer to the same dictionary in the memory
person_two = person_one.copy() #{'name': 'Prithvi', 'age': 22, 'gender': 'Male', 'hobbies': 'Football', 'language': 'javscript'}
person_one is person_two #False

#fromKeys. Creates a key value pair. Normally used to assign default values in a dictionary.
person_three = {}.fromkeys(["name","age","gender","hobbies","language"],"default")

# GET: used to access a value from the dictionary. Preferrable method since it doesnt throw an
#       error if the value doesn't exist
person_one.get("name") # Prithvi
person_one.get("activity") #None

# POP: removes the value from the dictionary with the specified key.
person_one.pop("hobbies") # removes hobbies from person_one

#POPITEM: popitem takes no argument, it removes the last element in the dictionary.
person_one.popitem() #removes the last item.

#UPDATE: updates the dictionary with the given values, without overriding the previous values
#        Only adds and updates never removes.
person_four = {}
person_four.update({"city" : "New Delhi"}) #adds city to person_four
person_four.update(person_one) #adds the person_one details to person_four
person_four.update({"name" : "Virat"}) #updates the name to Virat





