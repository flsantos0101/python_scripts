#Print product of 4 numbers if they are all prime

a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)

aux = 1
list = [a,b,c,d]

for i in list:
    if i > 1:
        isPrime = True
        for x in range(2,i):
            if i % x == 0:
                isPrime = False
        if isPrime == True:
            aux *= i
        else:
            break
    else:
        isPrime = False
        break

if isPrime == False:
    print('NO PRODUCT')
else:
    print(aux)
        

    