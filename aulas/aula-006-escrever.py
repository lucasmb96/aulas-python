import os
os.system('cls')

# Para criar/escrever ou ler num ficheiro é necessario
# 1º criar uma vriavel que represente o caminho do ficheiro
# Caminho abosluto - representa todo o percurso desde o disco C: até ao ficheiro

# Caminho relativo - representa o percuros desde a pasta do projeto até ao ficheiro

from pathlib import Path

ficheiro = Path(r'aulas\teste.txt')

# Utilizar o bloco with para abrir o ficheiro realizar as operações e fecha lo
# com o bloco with 
# open(modo de abertura, encoding, o que fazer caso haja erros)
# Modo de abertura
# 1 - Read - 'r'
# 2 Write - 'w'
# Append - 'a'

with ficheiro.open('w', encoding = 'utf-8', errors = 'ignore') as file:
    file.write('Olá turma!')

