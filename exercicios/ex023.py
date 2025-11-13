import os

os.system('cls')

count_num = 0
soma = 0
maior = 0
menor = 0

print('Programa de números ¯\_ (ツ)_/¯')
print('Inserir 0 para terminar')
# Teste para primeiro número inserido igual a zero
valor = int(input('Número: '))
if valor == 0:
    print(f'Inseriu 0 números\nNão há soma\nNão há maior nem menor')
# Atribuição inicial de valores para variaveis soma, menor e maior
else:
    soma += valor
    menor = valor
    maior = valor
    count_num += 1
    while valor != 0: 
        valor = int(input('Número: ')) # pedido de valor
        soma += valor # soma do valor á variavel
        if valor > maior and valor != 0: # atribuição de maior/menor valor ás variaveis
            maior = valor
        else:
            if valor < menor and valor != 0:
                menor = valor
        count_num += 1 # incremento de contador
    print(f'Inseriu {count_num-1} números\nA soma deles dá {soma}\nO maior número inserido foi {maior}\nO menor número inserido foi {menor}')


