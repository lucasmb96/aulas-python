import os

# limpar terminal
os.system('cls')

# print do titulo
print('--- Calculadora de ICM ---')

# pedir valores altura e peso ao utilizador
altura = float(input('Insira a sua altura em metros: '))
peso = float(input('Insira o seu peso em kilogramas: '))

# calculo do valor ICM
if(peso <= 0 or altura <= 0):
    print('Peso e altura devem ser maiores que zero.')
else:
    icm = peso / (altura * altura) # altura * altura é altura^2

# uso de condicionais if/else elif para imprimir respostas com linha print diretamente abaixo

print(f'O seu IMC é: {icm:.2f}')
if(icm < 18.5): # testa se valor icm está abaixo de 18.5 e imprime Abaixo de peso
    print('Abaixo do peso')
elif(icm >= 18.5 and icm < 25): # testa se valor icm está entre 18.5(incluido) e 24.99 e imprime Peso normal
    print('Peso normal')
elif(icm >= 25 and icm < 30): # testa se valor icm está entre 25(incluido) e 29.99 e imprime Sobrepeso
    print('Sobrepeso')
elif(icm >= 30 and icm < 35): # testa se valor icm está entre 30(incluido) e 34.99 e imprime Obesidade grau 1
    print('Obesidade grau 1')
elif(icm >= 35 and icm < 40): # testa se valor icm está entre 35(incluido) e 39.99 e imprime Obesidade grau 2
    print('Obesidade grau 2')
elif(icm >= 40): # testa se valor icm está acima de 40(incluido) e imprime Obesidade grau 3 (obesidade mórbida)
    print('Obesidade grau 3 (obesidade mórbida)')