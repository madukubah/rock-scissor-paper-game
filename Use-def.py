def input_player():
    player = int(input("PLAYER 1 CHOOSES: "))
    player2 = int(input("PLAYER 2 CHOOSES: "))
    return player, player2


def whos_win(player=0, player2=0):
    # 0 -> draw
    # 1 -> player 1 wins
    # 2 -> player 2 wins
    winner = 0
    if player == player2:
        winner = 0
        return winner

    if player == 1:  # rock
        if player2 == 2:  # paper
            winner = 2
        else:
            winner = 1
        return winner

    if player == 2:  # paper
        if player2 == 1:  # rock
            winner = 1
        else:
            winner = 2
        return winner

    if player == 3:  # scissors
        if player2 == 1:  # rock
            winner = 2
        else:
            winner = 1
        return winner

    return winner


def display(option='menu', username='player 0', player=0, winner=0):
    if option == 'menu':
        print('''ROCK PAPER SCISSORS GAME
ENTER YOUR CHOICE
|1 -> ROCK
|2 -> PAPER
|3 -> SCISSORS''')
    elif option == 'pilih':
        print(username, end=' ')
        if player == 1:
            print('CHOOSES -> ROCK')
        elif player == 2:
            print('CHOOSES -> PAPER')
        else:
            print('CHOOSES -> SCISSORS')
    else: # assuming only winner option is left
        if winner == 0:
            print('TIE')
        else:
            print(f'WINNER IS: PLAYER {winner}')

    return 1


def gameLoop():
    display()
    player, player2 = input_player()
    display('pilih', 'PLAYER 1', player)
    display('pilih', 'PLAYER 2', player2)

    winner = whos_win(player, player2)

    display('winner', winner=winner)

gameLoop()
