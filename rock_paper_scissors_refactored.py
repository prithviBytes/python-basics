import random

rand_int = random.randint(0,2)

if rand_int == 0:
    computer = "rock"
elif rand_int == 1:
    computer = "paper"
else:
    computer = "scissors"

print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Make your choice : ").lower()

print(f"Computer has selected {computer}")

if player == computer:
    print("its a tie!!!")
elif player == "rock":
    if computer == "scissors":
        print("player wins!!!")
    if computer == "paper":
        print("computer wins!!!")
elif player == "scissors":
    if computer == "paper":
        print("player, wins!!!")
    if computer == "rock":
        print("computer Wins!!!")
elif player == "paper":
    if computer == "scissors":
        print("computer wins")
    if computer == "rock":
        print("player wins!!!")
else:
    print("Something went wrong!!!")