str1 = input()
l = ['0','1','2','3','4','5','6','7','8','9']
aux = 0
for i in str1:
    if i in l:
        aux += 1
print(aux)
    