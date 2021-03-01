colors = ["orange"]

#******************************************ADDING AN ELEMENT***********************************
# APPEND:-  Adding one element to end of the list
colors.append("green")


# EXTEND:- Adding list of elements at the end of a list
colors.extend(["red","purple"])

# INSERT:- Insert an item at a particular position
colors.insert(1,"I came in between")

#******************************************DELETING AN ELEMENT***********************************
# CLEAR:- Removes all the items from the list
colors.clear()

colors = ['orange', 'I came in between', 'green', 'red', 'purple']

# POP:- Removes a paritcular element from the list if index is provides.
#          Else removes the last element.
#          In both cases it returns the removed element
colors.pop() #removes the last element
colors.pop(1) #removes the element at index 1

colors = ['orange', 'I came in between', 'green', 'red', 'purple']

# REMOVE:- removes the first mentioned item in the list.
#           throws an error if the element is not found.
colors.remove("green")
#colors.remove("green") Throws an error

#******************************************OTHER LIST METHODS***********************************

#INDEX:- returns the index of the specified item.
colors.index("purple")
# can specify starting index to look for
colors.index("purple",1)
#Can specify ending index as well
colors.index("purple",1,4)

#COUNT:-  Specifies the number of times a item appears in the list.
colors.count("red")

#REVERSE: reverses the list
colors.reverse()

#SORT: Sorts the array in ascending order.
colors.sort()

#JOIN: Joins the items in the array to form a string.
" ".join(colors)


#*********************************INTERMEDIATE METHODS***********************************

#SLICING: some_list[start:end:step]
#   start: some_list[start:] --- includes the start element as well.
#          for negative number it slices the list from the end.
#   end: some_list[:end] --- returns list before that number. Excluding the number.
#   step: some_list[::step] --- skips the specified number of elements in between

colors[0::1]

# Swapping values

names = ["James","Lily"]

names[0] , names[1] = names[1] , names[0]
