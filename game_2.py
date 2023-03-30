import random

def input_player_choice(player_name):
    while True:
        choice = input(f"{player_name}, choose rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        else:
            print("Invalid choice. Try again.")

def input_player_name(player_number):
    return input(f"Enter name for Player {player_number}: ")

def whos_win(player_choice, computer_choice):
    # 0 ->  draw
    # 1 ->  player 
    # 2 ->  computer
    winner = 0
    win_dict = {
        ('rock', 'rock'): 0, ('rock', 'paper'): 2, ('rock', 'scissors'): 1,
        ('paper', 'rock'): 1, ('paper', 'paper'): 0, ('paper', 'scissors'): 2,
        ('scissors', 'rock'): 2, ('scissors', 'paper'): 1, ('scissors', 'scissors'): 0
    }
    if player_choice != computer_choice:
        winner = win_dict[(player_choice, computer_choice)]
    return winner

def display_game_rules():
    print("WELCOME TO ROCK-PAPER-SCISSORS GAME")
    print("===================================")
    print("Game rules: ")
    print("1. Players choose either rock, paper, or scissors")
    print("2. Rock beats scissors, scissors beats paper, and paper beats rock")
    print("3. If the player chooses the same as the computer, it's a tie")
    print()

def single_player_game():
    display_game_rules()
    options = ['rock', 'paper', 'scissors']
    while True:
        player_choice = input_player_choice("Player")
        computer_choice = random.choice(options)
        print(f"Player chooses {player_choice}")
        print(f"Computer chooses {computer_choice}")
        winner = whos_win(player_choice, computer_choice)
        if winner == 0:
            print("It's a tie!")
        elif winner == 1:
            print("You win!")
        else:
            print("Computer wins!")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Thanks for playing!")

def two_player_game():
    display_game_rules()
    while True:
        player1_choice = input_player_choice("Player 1")
        player2_choice = input_player_choice("Player 2")
        print(f"Player 1 chooses {player1_choice}")
        print(f"Player 2 chooses {player2_choice}")
        winner = whos_win(player1_choice, player2_choice)
        if winner == 0:
            print("It's a tie!")
        elif winner == 1:
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("Thanks for playing!")

def main():
    print("1. Single player")
    print("2. Two player")
    choice = input("Enter your choice: ")
    if choice == '1':
        single_player_game()
    elif choice == '2':
        two_player_game()
    else:
        print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
