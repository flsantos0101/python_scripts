n = int(input())

values = input()
values = values.split(' ')
values = [int(i) for i in values]

#reverse

reversed = ''
values_reversed = values[::-1]
for i in values_reversed:
    reversed += str(i) + ' '
reversed = reversed[:-1]

#start from 2nd element

from_second = ''
values_from_second = values[1::]
values_from_second.append(values[0])
for i in values_from_second:
    from_second += str(i) + ' '
from_second = from_second[:-1]

#descending order

descending = ''
values_descending = values
values_descending.sort(reverse=True)
for i in values_descending:
    descending += str(i) + ' '
descending = descending[:-1]

print(reversed)
print(from_second)
print(descending)

