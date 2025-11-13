from pathlib import Path

caminho = Path(r'delfina.txt')

with caminho.open('w', encoding = 'utf-8', errors = 'ignore') as file:
    file.write('A Delfina está atenta!')

# ler ficheiros

with caminho.open('r', encoding = 'utf-8', errors = 'ignore') as file:
    for linha in file:
        print(linha)

caminho.rename(r'fans.txt')