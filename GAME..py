import random
bot = ['rock','scissors','paper']

while True:
    x = random.choice(bot)
    data = input('enter options: ')
    if data.lower() == x:
        print(f'your choice is {data.capitalize()}')
        print(f'Bot selection is {x.capitalize()}')
        print("draw\n\n")

    #saat menang
    elif data.lower() == 'rock' and x == 'scissors':
        print(f'your choice is {data.capitalize()}')
        print(f'Bot selection is {x.capitalize()}')
        print("you win\n\n")
    elif data.lower() == 'paper' and x == 'rock':
        print(f'your choice is {data.capitalize()}')
        print(f'Bot selection is {x.capitalize()}')
        print("you win\n\n")
    elif data.lower() == 'scissors' and x == 'paper':
        print(f'your choice is {data.capitalize()}')
        print(f'Bot selection is {x.capitalize()}')
        print("you win\n\n")

    #saat kalah
    elif data.lower() == 'scissors' and x == 'rock':
        print(f'your choice is {data.capitalize()}')
        print(f'Bot selection is {x.capitalize()}')
        print("you lose\n\n")
    elif data.lower() == 'rock' and x == 'paper':
        print(f'your choice is {data.capitalize()}')
        print(f'Bot selection is {x.capitalize()}')
        print("you lose\n\n")
    elif data.lower() == 'paper' and x == 'rock':
        print(f'your choice is {data.capitalize()}')
        print(f'Bot selection is {x.capitalize()}')
        print("you lose\n\n")

    else:
        print("invalid data\n\n")