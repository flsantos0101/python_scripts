n = int(input())

def is_Prime(n):
    is_Prime = True
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                is_Prime = False
                break
    else:
        is_Prime = False
    return is_Prime

def next_prime(n):
    aux = n
    while aux >= n:
        if is_Prime(aux) == True:
            return aux
            break
        else:
            aux += 1

def fact(n):
    prod = 1
    if n == 0 or n == 1:
        return prod
    else:
        for i in range(2,n+1):
            prod *= i
        return prod

series_sum = 0
series = ''

for i in range(1,n+1):
    if i == 1:
        series += ('%.f!' % i) + ('/%.f' % 1)
        series_sum += 1
    elif i == n:
        series += ('%.f!' % i) + ('/%.f' % next_prime(i))
        series_sum += fact(i)/next_prime(i)
    else:
        series += ('%.f!' % i) + ('/%.f + ' % next_prime(i))
        series_sum += fact(i)/next_prime(i)

if series == '1!/1 + ':
    series = '1!/1'
           
    
print(series)
print('%.2f' % series_sum)


