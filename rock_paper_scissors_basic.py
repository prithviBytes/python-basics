print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player1, Make your choice : ")
player2 = input("Player2, Make your choice : ")

if player1 == "rock" and player2 == "scissors":
    print("Player1 wins!!!")
elif player2 == "rock" and player1 == "scissors":
    print("Player2 wins!!!")
elif player1 == "scissors" and player2 == "paper":
    print("Player1, wins!!!")
elif player2 == "scissors" and player1 == "paper":
    print("Player2, wins!!!")
elif player1 == "paper" and player2 == "rock":
    print("Player1 wins !!!")
elif player2 == "paper" and player1 == "rock":
    print("Player2 wins !!!")
elif player1 == player2:
    print("Its a Tie!!!")
else:
    print("Something went wrong try again!!!")