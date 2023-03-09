import random


def check_win(player, computer):
    if player == computer:
        return "draw"
    elif player == "rock":
        if computer == "paper":
            return "computer"
        else:
            return "player"
    elif player == "paper":
        if computer == "scissors":
            return "computer"
        else:
            return "player"
    elif player == "scissors":
        if computer == "rock":
            return "computer"
        else:
            return "player"


options = ["rock", "paper", "scissors"]


while True:
  
    player_choice = input("Choose rock, paper, or scissors: ").lower()

 
    if player_choice not in options:
        print("Invalid input. Try again.")
        continue

 
    computer_choice = random.choice(options)

   
    print("You chose", player_choice)
    print("Computer chose", computer_choice)

   
    result = check_win(player_choice, computer_choice)
    if result == "draw":
        print("It's a draw!")
    else:
        print(result, "wins!")

    
    play_again = input("Play again? (y/n)").lower()
    if play_again != "y":
        break

print("Thanks for playing!")
