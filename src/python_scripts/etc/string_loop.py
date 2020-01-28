str = input()
for i in range(0,len(str)):
    if i % 2 == 0:
        print(str)
    else:
        print(str[::-1])

