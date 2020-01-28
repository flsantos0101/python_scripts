n = int(input())

def even_recursive(n):
    if n == 0:
        print(0)
    else:
        even_recursive(n-1)
        if n % 2 == 0:
            print(n)


even_recursive(n)
