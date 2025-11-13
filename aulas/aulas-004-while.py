import os
opcao = ''
while opcao != 4:
    os.system('cls')
    print('---Menu---')
    print('[ 1 ] - Calculadora')
    print('[ 2 ] - Numeros primos')
    print('[ 3 ] - Numeros pares')
    print('[ 4 ] - Sair')
    opcao = int(input('---> '))
    if opcao == 1:
        print('Escolheu Calculadora')
    elif opcao == 2:
        print('Escolheu Numeros primos')
    elif opcao == 3:
        print('Escolheu numeros pares')
    elif opcao == 4:
        print('Escolheu sair...')
    _ = input('ENTER para continuar...')
print('Programa terminado')