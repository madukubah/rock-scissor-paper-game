import random

options = ["rock", "paper", "scissors"]
bot = random.choice(options)
player = False

print ("Welcome to rock paper scissor game!")
print ("===================================\n")
 
while player == False:
    player = input("pick your choice (rock, paper, scissors): ")
    print(f"\nYou chose {player}, bot chose {bot}.\n")

    if player == bot:
        print("Draw Game!")
    elif player == "rock":
        if bot == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player == "paper":
        if bot == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player == "scissors":
        if bot == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("Invalid input!")

    play_again=input("\nPlay Again(y/n)= ")
    if play_again=="y":
        player = False
        bot = random.choice(options)
    elif play_again=="n":
        print("Thanks for playing")
    else:
        print("invalid input")
