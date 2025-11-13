import os

os.system('cls')


def contagem(inicio, fim, passo):
    if passo <= 0:
        passo = 1
        print('Passo alterado para 1.')
    
    if inicio < fim:
        for c in range(inicio, fim+1, passo):
            print(c)
    else:
        passo = -passo
        for c in range(inicio, fim, passo):
            print(c)


contagem(1, 20, 2)
contagem(10, 0, 1)

i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

contagem(i, f, p)