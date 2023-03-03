import random
import os

player_score = 0
computer_score = 0

suit_obj = ["","Rock","Scissors","Paper"]
player_pick = None
while player_pick != 0:
    os.system("cls")
    print (f"player [{player_score}]:[{computer_score}] computer")
    for x in range (1,4):
        print (f"{x}. {suit_obj[x]}")
    print()
    print("0. Exit the game")
    player_pick = int(input(">> "))
    if player_pick != 0:
        print(f"You choose {suit_obj[player_pick]}")

        computer_pick = random.randint(1,3)
        print(f"computer choose {suit_obj[computer_pick]}")

        if player_pick == computer_pick:
            print("- The results are draw")
        else:
            if(player_pick == 1 and computer_pick == 2) or (player_pick == 2 and computer_pick == 3) or (player_pick == 3 and computer_pick == 1):
                print("- You win!!")
                player_score += 1
            else:
                print("- You lose")
                computer_score+= 1

        input ("enter to next >> ")
        
