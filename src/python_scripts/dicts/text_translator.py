while True:
    n = input().split()
    n = [int(i) for i in n]
    if n == [0,0]:
        break
    translator = {}

    for i in range(n[0]):
        keys = input().split()
        translator[keys[0]] = keys[2]

    for i in range(n[1]):
        text = input()
        for i in translator:
            if i in text:
                text = text.replace(str(i),translator.get(str(i)))
        print(text)