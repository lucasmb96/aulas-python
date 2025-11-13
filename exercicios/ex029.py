import os
os.system('cls')

matriz = []
sum_par = 0
sum_2col = 0
maior = 0

for i in range(0,3):
    linha = []
    for j in range(0,3):
        valor = int(input(f'Digite o número da linha {i+1}, coluna {j+1}: '))
        if valor % 2 == 0:
            sum_par += valor
        if j == 1:
            sum_2col += valor
        if i == 2 and valor > maior:
            maior = valor
        linha.append(valor)
    matriz.append(linha[:])
    linha.clear()

for i in range(0,3):
    for j in range(0,3):
        print(matriz[i][j], end='')
    print()

print(f'A soma dos valores pares é: {sum_par}')
print(f'A soma dos valores da segunda coluna é: {sum_2col}')
print(f'O maior valor da terceira linha é: {maior}')