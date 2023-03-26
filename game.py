import random

print("Welcome to Rock, Paper, Scissors game!")

options = ["rock", "paper", "scissors"]

while True:
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if player_choice not in options:
        print("Invalid input. Please try again.")
        continue
    
    computer_choice = random.choice(options)
    print(f"Computer chooses {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a draw!")
    elif player_choice == "rock":
        if computer_choice == "paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif player_choice == "paper":
        if computer_choice == "scissors":
            print("Computer wins!")
        else:
            print("You win!")
    elif player_choice == "scissors":
        if computer_choice == "rock":
            print("Computer wins!")
        else:
            print("You win!")
    
    play_again = input("Do you want to play again? (y/n) : ").lower()
    if play_again != "y":
        break

print("Thank you for playing yeyee!")