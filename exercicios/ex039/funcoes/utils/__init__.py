import os
import sys
from funcoes import matematicas

def cabecalho(txt):
    print('-' * 30)
    print(f'{txt:-^30}')
    print('-' * 30)


def limpa():
    os.system('cls')


def menu():
    while True:
        cabecalho('CALCULADORA')
        print('[ 1 ] – Tabuada')
        print('[ 2 ] – Calculadora')
        print('[ 3 ] – Numeros Pares')
        print('[ 4 ] – Sair')

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcoes.matematicas.tabuada()
        elif opcao == "2":
            funcoes.matematicas.calculadora()
        elif opcao == "3":
            funcoes.matematicas.numpares()
        elif opcao == "4":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")