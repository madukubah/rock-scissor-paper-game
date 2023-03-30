print "update baru"
def input_player(username):
    # print('input_player')
    choice = int(input(f"{username} CHOICE = "))
    return choice

def whos_win(player1=0, player2=0):
    # 0 ->  draw
    # 1 ->  player 1
    # 2 ->  player 2
    winner = 0
    if player1 == player2:
        winner = 0
        return winner

    if player1 == 1:  # rock
        if player2 == 2:  # paper
            winner = 2
        else:
            winner = 1
        return winner

    if player1 == 2:  # paper
        if player2 == 1:  # rock
            winner = 1
        else:
            winner = 2
        return winner
    if player1 == 3:  # scissor
        if player2 == 1:  # rock
            winner = 2
        else:
            winner = 1
        return winner

    return winner


def display(option="menu", username="player1 0", player1=0, winner=0):
    if option == "menu":
        print("ROCK PAPER SCISSORS GAME")
        print("INPUT YOUR CHOICE")
        print("1 -> ROCK")
        print("2 -> PAPER")
        print("3 -> SCISSORS")
    if option == "choose":
        if player1 == 1:
            print(f"{username} CHOOSE -> ROCK")
        if player1 == 2:
            print(f"{username} CHOOSE -> PAPER")
        if player1 == 3:
            print(f"{username} CHOOSE -> SCISSORS")
    if option == "winner":
        if winner == 0:
            print("DRAW!")
        if winner == 1:
            print("THE WINNER IS : PLAYER 1")
        if winner == 2:
            print("THE WINNER IS : PLAYER 2")
    return 1


def gameLoop():
    display("menu")
    player1 = input_player("PLAYER 1")
    display("choose", "PLAYER 1", player1)
    player2 = input_player("PLAYER 2")
    display("choose", "PLAYER 2", player2)

    winner = whos_win(player1, player2)
    display("winner", "-", 0, winner)

    return 1


gameLoop()