n = int(input())

while n != 0:
    db = {}
    for i in range(n):
        name = input()
        color_size = input()
        if color_size in db:
            aux = db[color_size]
            aux.append(name)
            db[color_size] = aux
        else:
            db[color_size] = [name]
    
    print('')

    if "white S" in db:
        aux = db.get('white S')
        for i in aux:
            print('white S', i)

    if "white M" in db:
        aux = db.get('white M')
        for i in aux:
            print('white M', i)

    if "white L" in db:
        aux = db.get('white L')
        for i in aux:
            print('white L', i)

    if "red S" in db:
        aux = db.get('red S')
        for i in aux:
            print('red S', i)

    if "red M" in db:
        aux = db.get('red M')
        for i in aux:
            print('red M', i)

    if "red G" in db:
        aux = db.get('red G')
        for i in aux:
            print('red G', i)


    n = int(input())
