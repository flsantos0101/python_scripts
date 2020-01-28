flights = {}
for i in range(37):
    flight = input().split()
    flights[int(flight[0])] = int(flight[1])

while True:
    booking = input().split()
    booking = [int(i) for i in booking]
    if booking[0] == 9999:
        break
    else:
        if booking[1] in flights and flights.get(booking[1]) != 0:
            flights[booking[1]] -= 1
            print(booking[0])
        else:
            print('INDISPONIVEL')

