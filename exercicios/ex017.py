import os
os.system('cls')
import time


print('--- Calculadora ---')
print('[ 1 ] - Tabuada')
print('[ 2 ] - Calculadora')
print('[ 3 ] - Números Pares')
print('[ 4 ] - Sair')

opcao = int(input('Escolha das seguintes opções: '))

# Tabuada ---------------------------------
if opcao == 1:
    os.system('cls')
    print('--- Tabuada ---')
    tabuada = int(input('Digite um número para a tabuada: '))
    print(f'{opcao} x 1 = {opcao * 1}')
    print(f'{opcao} x 2 = {opcao * 2}')
    print(f'{opcao} x 3 = {opcao * 3}')
    print(f'{opcao} x 4 = {opcao * 4}')
    print(f'{opcao} x 5 = {opcao * 5}')
    print(f'{opcao} x 6 = {opcao * 6}')
    print(f'{opcao} x 7 = {opcao * 7}')
    print(f'{opcao} x 8 = {opcao * 8}')
    print(f'{opcao} x 9 = {opcao * 9}')
    print(f'{opcao} x 10 = {opcao * 10}')
# ---------------------------------------

# Calculadora ---------------------------

elif opcao == 2:
    os.system('cls')
    print('--- Calculadora ---')
    numero1 = int(input('Digite o primeiro numero: '))
    operador = input('Digite o operador: ')
    numero2 = int(input('Digite o segundo numero: '))
    if operador == '+':
        print(f'{numero1} {operador} {numero2} = {numero1 + numero2}')
    if operador == '-':
        print(f'{numero1} {operador} {numero2} = {numero1 - numero2}')
    if operador == '*':
        print(f'{numero1} {operador} {numero2} = {numero1 * numero2}')
    if operador == '/' and numero2 != 0:
        print(f'{numero1} {operador} {numero2} = {numero1 / numero2}')
#---------------------------------------------------

# Números Pares
elif opcao == 3:
    os.system('cls')
    print('--- Números Pares ---')
    numero = int(input('Digite o numero: '))
    if numero % 2 == 0:
        print('O numero é par')
    else:
        print('O numero é impar')
#--------------------------------
# Sair --------------------------
elif opcao == 4:
    os.system('cls')
    print('Sair',end='',flush=True)
    time.sleep(0.5)
    print('.',end='',flush=True)
    time.sleep(0.5)
    print('.',end='',flush=True)
    time.sleep(0.5)
    print('.',end='',flush=True)
#--------------------------------
