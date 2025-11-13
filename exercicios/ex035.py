import os

os.system('cls')

def fatorial(numero, f):
    '''
    -> Calcula o fatorial de um numero com a npossibilidade de mostrar o processo
    :param numero: O valor fatorial
    :param mostra: Boolean para mostrar ou não o processo
    return: sem retorno
    '''
    resultado = 1
    for i in range(numero, 0, -1):
        resultado *= i
        if f == True:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return resultado


print(fatorial(5, False))