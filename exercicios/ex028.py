import os
os.system('cls')

matriz = []

for i in range(0,3):
    linha = []
    for j in range(0,3):
        valor = int(input(f'Digite o número da linha {i+1}, coluna {j+1}: '))
        linha.append(valor)
    matriz.append(linha[:])
    linha.clear()

for i in range(0,3):
    for j in range(0,3):
        print(matriz[i][j], end='')
    print()