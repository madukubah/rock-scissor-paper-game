import random

def input_player():
    # print('input_player')
    player = int(input("PILIH :"))
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
    
def display(option='menu', username='player 0', player=0, winner=0 ):
    if option=='menu':
        print('GAME SUIT')
        print('INPUT PILIHAN ANDA')
        print('|1 -> BATU')
        print('|2 -> KERTAS')
        print('|3 -> GUNTING')
    if option=='pilih':
        print(username)
        if player == 1:
            print(' MEMILIH -> BATU')
        if player == 2:
            print(' MEMILIH -> KERTAS')
        if player == 3:
            print(' MEMILIH -> GUNTING')
    if option=='pemenang':
        if winner == 0:
            print('SERI')
        if winner == 1:
            print('PEMENANGNYA ADALAH : PLAYER 1')
        if winner == 2:
            print('PEMENANGNYA ADALAH : PLAYER 2') 
    return 1

def gameLoop():
    display('menu')
    player = input_player()
    display('pilih', 'PLAYER 1' , player)
    player2 = random.randint(1, 3)
    display('pilih', 'PLAYER 2' , player2)
    
    winner = whos_win(player, player2 )
    
    display('pemenang', '-', 0, winner)
    
    return 1
    
gameLoop()
    
    