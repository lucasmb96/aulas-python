import os
os.system('cls')

numero = int(input('Digite o numero: '))

if numero % 2 == 0:
    print('O numero é par')
elif numero % 2 != 0:
    print('O numero é impar')