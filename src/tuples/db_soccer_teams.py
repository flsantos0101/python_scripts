entry = input()
db = {}
while entry != '*':
    aux = []
    entry = entry.split(',')
    if entry[0] in db:
        for i in db[entry[0]]:
            if i[0] == entry[1]:
                aux.append((i[0],i[1]+1))
            else:
                aux.append(i)    
    else:
        db[entry[0]] = [('gold',0),('silver',0),('bronze',0)]
        for i in db[entry[0]]:
            if i[0] == entry[1]:
                aux.append((i[0],i[1]+1))
            else:
                aux.append(i)
    db[entry[0]] = aux
    entry = input()

for i in db:
    aux2 = []
    for y in db[i]:
        aux2.append(y[1])
    # Dictionary keys must be immutable, so swaping them for lists will raise an error
    # All mutable data structures in Python are non hashable
    db[i] = tuple(aux2) 


l = [(k,v) for v,k in db.items()]
pos = 1
#[((),'')]
l.sort()

for i in l:
    print('%s)%s gold:%s silver:%s bronze:%s' % (pos,l[-1][1],l[-1][0][0],l[-1][0][1],l[-1][0][2]))
    l = l[:-1]
    pos += 1
