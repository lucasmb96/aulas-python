import os

os.system('cls')

def area(w, l):
    a = w * l
    print(f'A area é: {a}m2.')

w = float(input('Digite o comprimento do terreno: '))
l = float(input('Digite o largura do terreno: '))

area(w, l)