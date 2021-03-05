# all: checks if all items in a iterable is truthy
names = ["Crist","Charlie","Cassindra"]
all([name[0] == "C" for name in names]) #True
names.append("Tom")
all([name[0] == "C" for name in names]) #False

#any: checks if any of the items are truthy
any([name[0] == "T" for name in names]) #True

