from pyfiglet import figlet_format as formater
from termcolor import colored
valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")


def print_colored_art(msg, shade):
    if shade not in valid_colors:
        shade = "green"
    result = colored(formater(msg), shade)
    print(result)


text = input("Enter Something \n")
color = input("Enter a color \n").lower()
print_colored_art(text, color)
