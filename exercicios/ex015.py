import os
os.system('cls')

numero1 = int(input('Digite o primeiro numero: '))

numero2 = int(input('Digite o segundo numero: '))

if numero1 > numero2:
    print(f'O primeiro numero introduzido:{numero1} é maior')
elif numero1 < numero2:
    print(f'O segundo numero introduzido:{numero2} é maior')
elif numero1 == numero2:
    print(f'Os numeros são iguais')