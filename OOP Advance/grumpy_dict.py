class GrumpyDict(dict):

    def __repr__(self):
        print("Grumpy Dict")
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"You want {key}? Well it aint here!")

    def __setitem__(self, key, value):
        print("Stop Bothering me!")
        return super().__setitem__(key, value)


data = GrumpyDict({"city": "Mumbai", "state": "Maharashtra"})

print(data)
# Grumpy Dict
# {'city': 'Mumbai', 'state': 'Maharashtra'}


print(data['country'])
# You want country? Well it aint here!
# None

data['city'] = "Bangalore"
# Stop Bothering me

print(data)
#{'city': 'Bangalore', 'state': 'Maharashtra'}
    