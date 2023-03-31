def input_player():
    # print('input_player')
    player = int(input("CHOOISE(PLAYER1) :"))
    
    return player

def input_player2():
    # print('input_player')
    player2 = int(input("CHOOISE(PLAYER2) :"))
    
    return player2

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
        return winner
    
    if player == 2: # paper
        if player2 == 1: # rock
            winner = 1
        else:
            winner = 2
        return winner
    
    if player == 3: # scissor
        if player2 == 1: # rock
            winner = 2
        else:
            winner = 1
        return winner
        
    return winner
    
def display(option='option', username='player 0', player=0, winner=0 ):
    if option=='option':
        print('GAME ROCK PAPER SCISSOR')
        print('INPUT YOUR CHOICE')
        print('1 -> ROCK')
        print('2 -> PAPER')
        print('3 -> SCISSOR')
    if option=='chooise':
        print(username)
        if player == 1:
            print(' CHOOSE -> ROCK')
        if player == 2:
            print(' CHOOSE -> PAPER')
        if player == 3:
            print(' CHOOSE -> SCISSOR')
    if option=='winner':
        if winner == 0:
            print('DRAW')
        if winner == 1:
            print('THE WINNER IS : PLAYER 1')
        if winner == 2:
            print('THE WINNER IS : PLAYER 2') 
    return 1

def gameLoop():
    display('option')
    player = input_player()
    display('chooise', 'PLAYER 1' , player)
    player2 = input_player2()
    display('chooise', 'PLAYER 2' , player2)
    
    winner = whos_win(player, player2 )
    
    display('winner', '-', 0, winner)
    
    return 1


gameLoop()