aux = input()

aux = aux.split(' ')

for i in aux:
    i = int(i)
aux.sort(reverse=True)
print(aux)