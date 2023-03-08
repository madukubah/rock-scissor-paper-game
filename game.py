import random

print("WELLCOME TO ROCK-PAPER-SCISSORS GAME")
print("====================================")
print("Game rules: ")
print("1. Players choose either rock, paper, or scissors")
print("2. Rock beats scissors, scissors beats paper, and paper beats rock")
print("3. If the player chooses the same as the computer, it's a tie")
print()

options = ['rock', 'paper', 'scissors']

while True:
    # player choice
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if player_choice not in options:
        print("Invalid choice. Try again.")
        continue
    
    # computer choice
    computer_choice = random.choice(options)
    
    print()
    print(f"You choose {player_choice}")
    print(f"Computer choose {computer_choice}.")

    # check winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else :
        print("Computer win!")
    
    # play again
    print()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break

print("Thanks for playing!!!")