import os
os.system('cls')

lista = []
lista.append(int(input('Digite um número: ')))

for i in range(0, 4):
    num = int(input('Digite um número: '))
    for j in range (len(lista)):
        if num <= lista[j]:
            lista.insert(j,num)
            break
        elif num > lista[j] and j == len(lista)-1:
            lista.append(num)
            break
    
print(lista)