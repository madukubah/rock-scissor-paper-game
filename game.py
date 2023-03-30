def whos_win(player, player2):
    # 0 = scissors, 1 = rock, 2 = paper
    if player == player2:
        return 0
    elif player == 0 and player2 == 1:
        return 2
    elif player == 0 and player2 == 2:
        return 1
    elif player == 1 and player2 == 0:
        return 1
    elif player == 1 and player2 == 2:
        return 2
    elif player == 2 and player2 == 0:
        return 2
    elif player == 2 and player2 == 1:
        return 1
    else:
        return -1 # if input is not valid

# main program
print("Welcome to Rock-Paper-Scissors Game!")
print("Please enter player 1's choice: 0 = scissors, 1 = rock, 2 = paper")
player1 = int(input())
print("Please enter player 2's choice: 0 = scissors, 1 = rock, 2 = paper")
player2 = int(input())

# calling the whos_win() function and printing the result
result = whos_win(player1, player2)
if result == 0:
    print("Result: Draw")
elif result == 1:
    print("Result: Player 1 wins")
elif result == 2:
    print("Result: Player 2 wins")