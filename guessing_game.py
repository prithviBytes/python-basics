import random

random_number = random.randint(1,10)
guess = None

while True:
    guess = input("Choose a Number between 1 and 10 \n")
    guess = int(guess)

    if guess > random_number:
        print("Maybe try a bit lower!!!")
    elif guess < random_number:
        print(" A bit higher maybe!!!")
    else:
        print("Wow you guessed my mind!!!")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing!!!!")
            break

