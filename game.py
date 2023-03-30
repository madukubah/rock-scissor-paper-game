while True:
    print("WELLCOME TO ROCK-SCISSOR-PAPER GAME!")
    print('====================================')
    print("PLAYER 1, PLEASE CHOOSE (R)ock, (S)cissors, or (P)aper.")
    player1 = input("PLAYER 1 ENTER : ")
    print("PLAYER 2, PLEASE CHOOSE (R)ock, (S)cissors, or (P)aper.")
    player2 = input("PLAYER 2 ENTER : ")
    print('====================================')
    if player1 == player2:
        print("DRAW!!!!")
    elif player1 == "R":
        if player2 == "S":
            print("PLAYER 1 WIN!")
        else:
            print("PLAYER 2 WIN!")
    elif player1 == "S":
        if player2 == "P":
            print("PLAYER 1 WIN!")
        else:
            print("PLAYER 2 WIN!")
    elif player1 == "P":
        if player2 == "R":
            print("PLAYER 1 WIN!")
        else:
            print("PLAYER 2 WIN!")
    else:
        print("Invalid Input. Please enter R, S or P!")

    next = input("Do you want to play again? (y/n): ")
    if next == "n":
        break