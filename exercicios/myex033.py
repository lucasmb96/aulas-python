import os

os.system('cls')

def contagens(inicio, fim, passo):
    print(f'Contagem 1-20 de 2 em 2')
    for i in range(0, 20, 2):
        print(f'{i}')
    print(f'Contagem 10-0 de 1 em 1')
    for i in range(10, 0, -1):
        print(f'{i}')
    print(f'Contagem {inicio}-{fim} de {passo} em {passo}')
    for i in range(inicio, fim, passo):
        print(f'{i}')


recebe = []
inicio = int(input('Digite o inicio:'))
recebe.append(inicio)
fim = int(input('Digite o fim:'))
recebe.append(fim)
passos = int(input('Digite os passos:'))
recebe.append(passos)
print(recebe)

contagens(recebe)