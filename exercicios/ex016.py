from random import randint
import os
os.system('cls')

numero_random = randint(0,7)
numero_user = int(input('Digite um numero de 0 a 7: '))

if numero_random == numero_user:
    print(f'{numero_user} = {numero_random}')
    print(' !Venceu! :)')
else:
    print(f'{numero_user} != {numero_random}')
    print(' !Perdeu! :(')


