from pathlib import Path

caminho = Path(r'notas.txt')

notas_lista = []
for i in range (0, 5):
    notas_lista.append(float(input('Insira a nota: ')))

nomes = 'Ana', 'Carolina', 'Lucas', 'João', 'Miguel'

media = sum(notas_lista) / len(notas_lista)
maior = max(notas_lista)
menor = min(notas_lista)

with caminho.open('w', encoding = 'utf-8', errors = 'ignore') as file:
    for i in range(len(notas_lista)):
        file.write(f'A nota do aluno {nomes[i]} foi {notas_lista[i]}\n')
    file.write(f'A média das notas é: {media}\n')
    file.write(f'A maior nota é: {maior}\n')
    file.write(f'A menor nota é: {menor}\n')





