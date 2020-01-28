n = int(input())
db = {}

while n != 0:
    for i in range(n):
        nome = input()
        cor_tamanho = input()
        if cor_tamanho in db:
            aux = db[cor_tamanho]
            aux.append(nome)
            db[cor_tamanho] = aux
        else:
            db[cor_tamanho] = [nome]

    if "branco P" in db:
        aux = db.get('branco P')
        for i in aux:
            print('branco P', i)

    if "branco M" in db:
        aux = db.get('branco M')
        for i in aux:
            print('branco M', i)

    if "branco G" in db:
        aux = db.get('branco G')
        for i in aux:
            print('branco G', i)

    if "vermelho P" in db:
        aux = db.get('vermelho P')
        for i in aux:
            print('vermelho P', i)

    if "vermelho M" in db:
        aux = db.get('vermelho M')
        for i in aux:
            print('vermelho M', i)

    if "vermelho G" in db:
        aux = db.get('vermelho G')
        for i in aux:
            print('vermelho G', i)
    print('\n')

    n = int(input())
