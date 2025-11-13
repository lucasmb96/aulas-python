import os
from random import randint

os.system('cls')

numero_gerar = int(input('Quantos sorteios devo gerar? '))

chaves = {}


total = []

# perguntar operador
for i in range(0, numero_gerar):
    numeros = []
    estrelas = []
    while (len(numeros) < 5):
        n = randint(1, 50)
        if n not in numeros:
            numeros.append(n)
    while (len(estrelas) < 2):
        e = randint(1, 12)
        if e not in estrelas:
            estrelas.append(e)
    chaves = { "Números": numeros, "Estrelas" : estrelas }
    total.append(chaves)

for i in total:
    print(f'Chave:' )
    for j, k in chaves.items():
        print(f'{j} -> {k}')
