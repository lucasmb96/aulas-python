# tuples são imutaveis
# temos de iniciar com valores

turma = 'Delfina' , 'José' , 'Eduardo' , 'João'

print(type(turma)) #tuple

print(turma[0]) # Delfina

print('\n')

print('\nfor nome in turma:')
for indice, nome in enumerate(turma):
    print(f'No indice {indice} tem {nome}.')

print('\n\n')
if 'Delfina' in turma:
    print('Delfina está na turma')
else:
    print('Delfina não está na turma')

print(sorted(turma))
print(turma)
