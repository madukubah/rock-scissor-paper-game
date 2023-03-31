def input_player():
    player=int(input("Choose one : "))
    return player

def whos_win(player=0, player2=0):
    winner=0
    if player == player2:
        winner = 0
    elif player==1: #rock
        if player2==2: #paper
            winner=2
        else:
            winner=1
    elif player==3: #Scissor
        if player2==1: #rock
            winner=1
        else:
            winner=2
    elif player==2: #paper
        if player2==1: #rock
            winner=1
        else:
            winner=2
    return winner
    

def display(option='menu', username='player 0',player=0, winner=0):
    if option=='menu':
        print('RPS Game \n')
        print('Input your choice \n')
        print('|1-> Rock\n|2-> Paper\n|3-> Scissor')
    if option=='choice':
        print(username)
        if player==1:
            print("choice Rock")
        elif player==2:
            print("choice Paper")
        elif player==3:
            print("choice Scissor")
        else:
            print("ERROR!")
    if option=='winner':
        if winner == 0:
            print('DRAW')
        if winner == 1:
            print('The Winner is : PLAYER 1')
        if winner == 2:
            print('The Winner is : PLAYER 2') 
    return 1
        
def gameLoop():
    display('menu')
    player=input_player()
    display("choice", 'player 1' ,player)
    player2 = input_player()
    display("choice", 'player 2' ,player2)
    winner = whos_win(player, player2)
    display('winner','Thanos', 0, winner)
    return 1
    
gameLoop()