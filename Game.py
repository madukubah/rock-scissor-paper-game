import random

player_score = 0
computer_score = 0

while True:
    print("Welcome Yudhy, to the rock paper scissors game")
    print()

    player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    while player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice.")
        player_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"The computer chooses {computer_choice}.")

    if player_choice == computer_choice:
        print("It's a tie!") #untuk memisahkan sebuah statement yang panjang menjadi 
        #beberapa baris tanpa harus menuliskan semuanya dalam satu baris (continuation character)
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("Result: You win!")
        player_score += 1
    else:
        print("Result: You lose.")
        computer_score += 1

    print(f"Score: Player {player_score} - Computer {computer_score}")
    print()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "no":
        break
print("Thank you for playing!")