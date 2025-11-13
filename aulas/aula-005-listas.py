tuplos = [1,2,3,4,5]
print(type(tuplos))
'''
lista_nomes = ['Delfina', 'Jorge', 'Bruno', 'João']
for nome in lista_nomes:
    print(nome)

for indice, nome in enumerate(lista_nomes):
    print(f'{indice} -> {nome}')

print('Delfina' in lista_nomes)
'''

lista_nomes = list()
for c in range(0, 10):
    nome = input('Digite um nome: ')
    if nome in lista_nomes:
        print('Nome já está na lista')
    else:
        print('Nome adicionado com sucesso')
        lista_nomes.append(nome)