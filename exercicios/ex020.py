import os

os.system('cls')

# pede número inteiro
num = int(input('Digite um número: '))

var_bool = True

if num <= 1:
    var_bool = False
else:
    for t in range(2,num):
        if num % t == 0:
            var_bool = False
            break
        else:
            var_bool = True

if var_bool == True:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')