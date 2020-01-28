def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        a, b = 1, 2
        for i in range(2,n):
            a, b = b, a+b
        return b

n = int(input())
print(fib(n))

