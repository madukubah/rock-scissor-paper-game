import random

def input_player(player_num):
    valid_input = False
    while not valid_input:
        player_input = input(f"Player {player_num}, pilih (1) Batu, (2) Gunting, atau (3) Kertas: ")
        if player_input in ['1', '2', '3']:
            valid_input = True
            return int(player_input)
        else:
            print("Invalid input")

def whos_win(player1, player2):
    if player1 == player2:
        return 0
    elif (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 3) or (player1 == 3 and player2 == 1):
        return 1
    else:
        return 2

def display_menu():
    print('Janken Game')
    print('============================')
    print('player 1, choose your option:')
    print('(1) Batu')
    print('(2) Gunting')
    print('(3) Kertas')
    print()

def display_round(player1, player2, winner):
    print(f'player 1 choose: {get_choice_text(player1)}')
    print(f'player 2 choose: {get_choice_text(player2)}')
    if winner == 1:
        print('Pemain 1 menang!')
    elif winner == 2:
        print('Pemain 2 menang!')
    else:
        print('Seri!')

def get_choice_text(choice):
    if choice == 1:
        return 'Batu'
    elif choice == 2:
        return 'Gunting'
    else:
        return 'Kertas'

def play_game():
    display_menu()
    player1 = input_player(1)
    player2 = input_player(2)
    winner = whos_win(player1, player2)
    display_round(player1, player2, winner)
    return winner

def play_again():
    play_again = input("Apakah Anda ingin bermain lagi? (y/n) ")
    return play_again.lower() == 'y'

def game_rounds():
    score = {'Player 1': 0, 'Player 2': 0, 'Ties': 0}
    play_more = True
    while play_more:
        winner = play_game()
        if winner == 1:
            score['Player 1'] += 1
        elif winner == 2:
            score['Player 2'] += 1
        else:
            score['Ties'] += 1
        print(f"Skor: Player 1: {score['Player 1']}, Player 2: {score['Player 2']}, Seri: {score['Ties']}")
        print()
        play_more = play_again()
    print('Thanks to play!')

game_rounds()
