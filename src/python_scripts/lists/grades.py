n = int(input())

l = []

for i in range(n):
	num = int(input())
	l.append(num)

sum = 0
length = 0

for i in l:
	sum += i
	length += l

mean = sum/length

aux1 = 0
axu2 = 0

for i in l:
	if i > 1.1*mean:
		aux1 += 1
	if i< 0.9*mean:
		aux2 += 1

print('%0.2f' % mean)
print(aux1)
print(aux2)

