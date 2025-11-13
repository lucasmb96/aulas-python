import os

os.system('cls')

sum = 0

for t in range(0,5):
    sum = sum + int(input(f'{t+1}º Número: '))

print(int(sum))