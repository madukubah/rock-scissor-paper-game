angka=int(input('masukan tujuan angka:'))
total=0
counter=0
for i in range(1,angka+1):
    if i%2==0 and i%5==0:
        print(i,end='')
        total+=i
        counter+=1
        if(counter!=angka//10):
            print(' + ',end='')
print(' = ',total)

