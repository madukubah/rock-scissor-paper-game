def input_player():
    # print('input_player')
    player = int(input("INPUT YOUR CHOICE : "))
    return player

def whos_win(player=0, player2=0  ):
    # 0 ->  draw
    # 1 ->  player 1
    # 2 ->  player 2
    winner = 0
    if player == player2:
        winner = 0
        return winner
    
    if player == 1: # rock
        if player2 == 2: # paper
            winner = 2
        else:
            winner = 1
    elif player == 2: # paper
        if player2 == 1: # rock
            winner = 1
        else:
            winner = 2
    elif player == 3: # scissor
        if player2 == 1: # rock
            winner = 2
        else:
            winner = 1
    return winner


def display(option='menu', username='player 0', player=0, winner=0 ):
    if option=='menu':
        print('WELCOME TO ROCK PAPER SCISSOR GAME!!')
        print('PICK YOUR CHOICE (ROCK, PAPER, SCISSOR)\n')
        print('|1 -> ROCK')
        print('|2 -> PAPER')
        print('|3 -> SCISSOR\n')
    if option=='choice':
        print(username)
        if player == 1:
            print(' YOUR CHOICE ROCK\n')
        if player == 2:
            print(' YOUR CHOICE PAPER\n')
        if player == 3:
            print(' YOUR CHOICE SCISSOR\n')
    if option=='winner':
        if winner == 0:
            print('DRAW')
        if winner == 1:
            print('THE WINNER IS PLAYER 1')
        if winner == 2:
            print('THE WINNER IS PLAYER 2') 
    return 1

def gameLoop():
    display('menu')
    player = input_player()
    display('choice', 'PLAYER 1' , player)
    player2 = input_player()
    display('choice', 'PLAYER 2' , player2)
    
    winner = whos_win(player, player2 )
    
    display('winner', '-', 0, winner)
    
    return 1
gameLoop()