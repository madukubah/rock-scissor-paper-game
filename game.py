import random
import os

os.system('cls')
print("------Rock Scissor Paper------")
print('1.Rock')
print('2.Scissor')
print('3.Paper')
print('------------------------------')

choice = int(input('Input your choice (1/2/3): '))
computer = random.choice(["Rock","Scissor","Paper"])

if choice == 1:
    print('User     : Rock')
    print('Computer :', computer)
    if computer == 'Rock':
        print('same result')
    elif computer == 'Scissor':
        print('You win')
    elif computer == 'Paper':
        print('You lose')
        
elif choice == 2:
    print('User     : Scissor')
    print('Computer :', computer)
    if computer == 'Rock':
        print('You lose')
    elif computer == 'Scissor':
        print('same result')
    elif computer == 'Paper':
        print('You win')

elif choice == 3:
    print('User     : Paper')
    print('Computer :', computer)
    if computer == 'Rock':
        print('You win')
    elif computer == 'Scissor':
        print('You lose')
    elif computer == 'Paper':
        print('same result')
        
else:
    print('no options!')
