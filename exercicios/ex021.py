import os

os.system('cls')

frase = input('Escreva a frase: ').replace(' ','').lower()

len_frase = len(frase)

for i in range (0,len(frase)):
    if frase[i] != frase[len_frase - i - 1] and len_frase - i - 1 != i:
        print('Não é um palíndromo')
if i == len(frase) - 1:
    print('É um palíndromo')