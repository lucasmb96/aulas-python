import os

os.system('cls')

print('---------------')
print('---Cabeçalho---')

def cabecalho(msg):
    separador()
    print(f'--- {msg} ---')
    separador()


def contador(*num):
    soma = 0
    for numero in num:
        soma += numero
    
    print(f'A soma dos valores é: {soma}')

def mostra_lista(lista):
    for numero in lista:
        print(f'-> {numero}')


valores =[1,2,3,4,5,6,7]
#contador(1,2,3)
mostra_lista(valores)