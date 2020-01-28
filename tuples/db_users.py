number_of_inputs = int(input())
db = {}

for i in range(number_of_inputs):
    age = int(input())
    char_name = input()
    sex = input()
    marital_status = input()
    friends = int(input())
    photos = int(input())
    info = tuple((age,sex,marital_status,friends,photos))
    db[char_name] = info

for i in db:
    aux = db.get(i)
    print('Idade: %.f' % aux[0])
    print('Nome: %s' % i)
    print('Sexo: %s' % aux[1])
    print('Estado Civil: %s' % aux[2])
    print('Numero de amigos: %.f' % aux[3])
    print('Numero de fotos: %.f\n' % aux[4])