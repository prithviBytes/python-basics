from random import randint

print("...rock...")
print("...paper...")
print("...scissors...")

computer_wins = 0
player_wins = 0


while player_wins < 2 and computer_wins < 2:
    for times in range(0,3):
        print(f"Player score {player_wins} & Computer score {computer_wins}")
        player_choice = input("Enter your choice: ").lower()
        random_number = randint(0,2)

        if random_number == 0:
            computer_choice = "rock"
        elif random_number == 1:
            computer_choice = "paper"
        else:
            computer_choice = "scissors"

        print(f"Computer plays {computer_choice}")

        if player_choice == computer_choice:
            print("Its a Tie!!!")
        elif player_choice == "rock":
            if computer_choice == "scissors":
                player_wins += 1
                print("You win")
            else:
                computer_wins += 1
                print("Computer Wins!!!")
        elif player_choice == "paper":
            if computer_choice == "rock":
                player_wins += 1
                print("You win!!!")
            else:
                computer_wins += 1
                print("Computer Wins!!!")
        elif player_choice == "scissors":
            if computer_choice == "paper":
                player_wins += 1
                print("You win!!!")
            else:
                computer_wins += 1
                print("Computer Wins!!!")
        else:
            print("Please enter a valid choice")
        if player_wins == 2 or computer_wins == 2:
            break
if player_wins == 2:
    print("Player Wins The Battle!!!")
else:
    print("Computer Wins the Battle!!!")