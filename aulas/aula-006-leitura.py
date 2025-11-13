from pathlib import Path

ficheiro = Path(r'aulas\10270.log')

with ficheiro.open('r', encoding='utf-8', errors = 'ignora') as file:
    for linha in file:
        if 'error' in linha.lower():
            print(linha, end='')



