from pathlib import Path

ficheiro = Path(r'aulas\10270.log')
saida = r'out.txt'

with ficheiro.open('r', encoding='utf-8', errors = 'ignora') as file:
    
    out = open(saida,'w', encoding='utf-8', errors = 'ignora')

    for linha in file:
        if 'error' in linha.lower():
            out.write(linha)

out.close()