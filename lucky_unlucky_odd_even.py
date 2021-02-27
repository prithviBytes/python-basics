for num in range(1,21):
    if num == 4 or num == 13:
        type = "unlucky"
    elif num % 2 == 0:
        type="even"
    else:
        type="odd"
    
    print(f"{num} is a {type} number")