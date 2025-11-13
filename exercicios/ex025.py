import os
os.system('cls')

cla = (
    "Barcelona", "Real Madrid", "Atlético Madrid", "Athletic Club", "Villarreal",
    "Real Betis", "Celta Vigo", "Rayo Vallecano", "Osasuna", "Mallorca",
    "Real Sociedad", "Valencia", "Getafe", "Espanyol", "Alavés",
    "Girona", "Sevilla", "Leganés", "Las Palmas", "Real Valladolid"
)

print('-- 5 Primeiras equipas --')
for indice, equipa in enumerate(cla):
    if indice == 5:
        break
    print(f'\t- {indice}º - {equipa}')

print('-- 4 Ultimas equipas --')
TAM = len(cla)
for indice, equipa in enumerate(cla):
    if indice >= TAM -4:
        print(f'\t- {indice+1}º - {equipa}')
    else:
        continue # passa para a próxima interação

for equipa in sorted(cla):
    print(f'{equipa}', end=' | ')

print('\n')

if 'Las Palmas' in cla:
    print(f'Las Palmas está na {cla.index('Las Palmas') + 1}º posição')
else:
    print('Las Palmas não está na lista')