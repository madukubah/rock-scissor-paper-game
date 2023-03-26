import random


# variable
index = ['rock', 'paper', 'scissor']
# user computer
computer = random.choice(index)
# set variabel player = false
player = False

while player == False :
    # enter player selection
    player = input("rock, paper, scissor = ")
    if computer == player :
        print("player = ", computer)
        print("computer select = ", computer)
        print("draw game!!")
    elif player == 'rock':
        print("Player = rock")
        if computer == 'paper' :
            print("computer select paper")
            print("you lose!!!")
        else :
            print("computer select scissor")
            print("you win!!!")
    elif player == 'paper':
        print("Player = paper")
        if computer == 'scissor' :
            print("computer select scissor")
            print("you lose!!!")
        else :
            print("computer select rock")
            print("you win!!!")
    elif player == 'scissor':
        print("Player = scissor")
        if computer == 'rock' :
            print("computer select rock")
            print("you lose!!!")
        else :
            print("computer selected papper")
            print("you win!!!")
    else:
        print("you choise wrong!!!, please reselect!!!")
    play_again=input('Play Again(y/n)= ')
    if play_again=='y':
        player = False
        computer = random.choice(index)
    elif play_again=='n':
        print("Game Over")
        break