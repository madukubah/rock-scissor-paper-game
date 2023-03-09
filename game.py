import random

options = ['rock', 'paper', 'scissors']

print("Welcome to rock🪨, paper📃, scissors✂️!")

# Start looping (While)
while True:

    # user choices
    player_choice = input("\nChoose your weapon (rock, paper, or scissors): ")
    if player_choice not in options:
        print("Invalid choice. Try again!")
        continue

# computer choices
    computer_choice = random.choice(options)

    print(f"\nYou chose {player_choice}.")
    print(f"The computer chose {computer_choice}.")

# check winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 'rock':
        if computer_choice == 'paper':
            print("Paper covers rock. You lose!")
        else:
            print("Rock smashes scissors. You win!")
    elif player_choice == 'paper':
        if computer_choice == 'scissors':
            print("Scissors cut paper. You lose!")
        else:
            print("Paper covers rock. You win!")
    elif player_choice == 'scissors':
        if computer_choice == 'rock':
            print("Rock smashes scissors. You lose!")
        else:
            print("Scissors cut paper. You win!")

# play again
    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again.lower() != 'y':
        break

print("Thanks for playing!")
