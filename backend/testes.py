import time

tempo = ["0-10","13","15-21"]
lista = []
for i in tempo:
    a = ''
    for j in i:
        if j == '-':
            b = a
            a = ''
        else:
            a = a + j
    
    if b:
        for i in range(int(b),int(a)):
            lista.append(i)
        b = ''
    else:
        lista.append(int(a))

for i in lista:
    print(f'{i} ')

        
