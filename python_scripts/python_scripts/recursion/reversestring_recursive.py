def reverse(str1):
    if str1 == '':
        return ''
    else:
        return str1[-1] + reverse(str1[:-1])

n = int(input())

for i in range(n):
    str1 = str(input())
    print(reverse(str1))
