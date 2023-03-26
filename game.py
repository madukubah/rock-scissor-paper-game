import random
import time
bot=['batu','guting','kertas']

print("hallo world".lower())
while True:
    x = random.choice(bot)
    data = input('Masukkan pilihan')
    if data.lower() == x: