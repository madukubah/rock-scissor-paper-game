import random


def input_player_name(player_name):
    while True:
        try:
            player = int(input(f"{player_name}, SELECT: "))
            if player in [1, 2, 3]:
                return player
            else:
                print("Invalid selection, enter a value between 1-3")
        except ValueError:
            print("Selection must be a number between 1-3")


def whos_win(player=0, player2=0):
    # 0 =>  draw
    # 1 =>  player 1
    # 2 =>  player 2
    winner = 0
    win_dict = {
        (1, 1): 0, (1, 2): 2, (1, 3): 1,
        (2, 1): 1, (2, 2): 0, (2, 3): 2,
        (3, 1): 2, (3, 2): 1, (3, 3): 0
    }
    if player != player2:
        winner = win_dict[(player, player2)]
    return winner


def display(option='menu', username='player 0', player=0, winner=0):
    if option == 'menu':
        print('\tGAME SUIT')
        print('INPUT YOUR CHOICES = ')
        print('1 => ROCK')
        print('2 => PAPER')
        print('3 => SCISSORS')
    if option == 'SELECT':
        print(username)
        if player == 1:
            print('\tSELECT => ROCK')
        if player == 2:
            print('\tSELECT => PAPER')
        if player == 3:
            print('\tSELECT => SCISSORS')
    if option == 'WINNER':
        if winner == 0:
            print('DRAW')
        if winner == 1:
            print('WINNER IS: PLAYER 1')
        if winner == 2:
            print('WINNER IS: PLAYER 2')
    return 1


def gameLoop():
    display('menu')
    player = input_player_name('PLAYER 1')
    display('SELECT', '\tPLAYER 1', player)
    player2 = input_player_name('PLAYER 2')
    display('SELECT', '\tPLAYER 2', player2)

    winner = whos_win(player, player2)

    display('WINNER', '-', 0, winner)

    return 1


gameLoop()
