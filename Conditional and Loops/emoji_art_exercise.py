# Using for loop
for count in range(1,11):
    print("\U0001f600" * count)

# Using while loop
count = 1
while count <= 10:
    print("\U0001f600" * count)
    count += 1

# Using both for and while loop
for num in range(1,11):
    count = 1 
    smileys = ""
    while count <= num:
        smileys += "\U0001f600"
        count += 1
    print(smileys)