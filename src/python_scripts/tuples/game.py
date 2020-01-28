number_of_inputs = int(input())
db = {}

for i in range(number_of_inputs):
    char_name = input()
    char_id = int(input())
    char_level = int(input())
    char_health = int(input())
    char_attack = int(input())
    char_defense = int(input())
    info = tuple((char_id,char_level,char_health,char_attack,char_defense))
    db[char_name] = info

for i in db:
    aux = db.get(i)
    print('Name: %s' % i)
    print('ID: %.f' % aux[0])
    print('Level: %.f' % aux[1])
    print('Health: %.f' % aux[2])
    print('Attack: %.f' % aux[3])
    print('Defense: %.f' % aux[4])
