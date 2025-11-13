import os
os.system('cls')

print('--- Introduzir números na lista ---')
print('0 para terminar')
lista = []
i = int(input('Introduza o número a inserir [0 para terminar]: '))
if i == 0:
    print('Não colocou número, terminar programa')
else:
    lista.append(i)
    while (i != 0):
        i = int(input('Introduza o número a inserir [0 para terminar]: '))
        for j in range (len(lista)):
            if i == 0:
                print('Introduziu 0, terminar programa...')
                break
            elif i <= lista[j]:
                lista.insert(j,i)
                break
            elif i > lista[j] and j == len(lista)-1:
                lista.append(i)
                break

print(lista)
