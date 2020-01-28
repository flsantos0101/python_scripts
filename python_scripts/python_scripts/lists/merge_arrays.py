n = int(input())

l1 = []
l2 = []

for i in range(n):
    num = int(input())
    l1.append(num)

for i in range(n):
    num = int(input())
    l2.append(num)

aux = []

for i in range(n):
    aux.append(l1[i])
    aux.append(l2[i])

for i in aux:
    print(i)


