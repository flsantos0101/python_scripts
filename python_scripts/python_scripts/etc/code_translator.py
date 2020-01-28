# Code translator
while True:
    code = input()
    code = code.split()
    intab = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    aux = ''
    for i in code:
        aux += intab[int(i)]
    if aux == 'fim':
        break
    print(aux)

