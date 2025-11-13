from pathlib import Path

caminho = Path(r'notas.txt')

with caminho.open('r', encoding = 'utf-8', errors = 'ignore') as file:
    for c in file:
        print(c, end = '')
