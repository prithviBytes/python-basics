# Bundles the arguments inside a dictionary. The arguments should be in key value
# pairs.

def fav_colors(**kwargs):
    for person,color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


fav_colors(prithvi="black",messi = "blue", ronaldo = "white")


