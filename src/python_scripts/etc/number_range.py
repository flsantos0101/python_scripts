a, b = input().split()
a, b = int(a), int(b)
aux = ''

for i in range(1,b+1):
    aux += str(i) + ' '
    if i % a == 0 and i != 0:
        aux = aux[:-1]
        aux += '\n'

print(aux)
    


    