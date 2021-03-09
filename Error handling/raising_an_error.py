def colorize(text,color):
    colors = ("red","green","purple")
    if color not in colors:
        raise ValueError(f"{color} doesn't exist")
    if type(text) is not str:
        raise TypeError("Text should be a string")
    print(f"{text} in color {color}")

colorize("Prithvi","black")