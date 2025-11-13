import os
from random import randint
from time import sleep

os.system('cls')

print('--- Jogo da Advinha ---')
sleep(0.5)
print('Tente descobrir o número ?')
sleep(2)

numero_random = randint(0,10)
contador = 0

while True:
    valor_user = int(input('A sua escolha: '))
    if valor_user == numero_random:
        print(f'O número {valor_user} é o correto e precisou de {contador+1} tentativas!')
        break
    else:
        if valor_user > numero_random:
            print(f'O número {valor_user} não é o correto e está acima!\nTente outra vez!')
            sleep(3)
            os.system('cls')
            contador += 1
        else:
            print(f'O número {valor_user} não é o correto e está abaixo!\nTente outra vez!')
            sleep(3)
            os.system('cls')
            contador += 1


