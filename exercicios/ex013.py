import os
os.system('cls')

velocidade = int(input('Digite a velocidade: '))

if velocidade <= 80:
    print('Não multado')

elif velocidade > 80:
    print(f'Multado com valor de {100 + (velocidade-80)*7}')