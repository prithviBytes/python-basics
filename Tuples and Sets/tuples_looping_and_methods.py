months = ('January','February','March','April','May','June','July','August','September','October','November','December')

for month in months:
    print(month)

i = 0
while i < len(months):
    print(months[i])
    i += 1

## COUNT: returns the number of specified items in the tuple.
months.count("January") # 1

## INDEX:  returns the index of the specified item.
months.index("February") # 1