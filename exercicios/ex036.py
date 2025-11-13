
import os

os.system('cls')

def calcula_IMC():
    # pedir valores altura e peso ao utilizador
    altura = float(input('Insira a sua altura em metros: '))
    peso = float(input('Insira o seu peso em kilogramas: '))
        # calculo do valor ICM
    if(peso <= 0 or altura <= 0):
        print('Peso e altura devem ser maiores que zero.')
    else:
        icm = peso / (altura * altura) # altura * altura é altura^2
    return icm


def tipo_corpo(imc):
    print(f'O seu IMC é: {imc:.2f}')
    if(imc < 18.5): # testa se valor imc está abaixo de 18.5 e imprime Abaixo de peso
        print('Abaixo do peso')
    elif(imc >= 18.5 and imc < 25): # testa se valor imc está entre 18.5(incluido) e 24.99 e imprime Peso normal
        print('Peso normal')
    elif(imc >= 25 and imc < 30): # testa se valor imc está entre 25(incluido) e 29.99 e imprime Sobrepeso
        print('Sobrepeso')
    elif(imc >= 30 and imc < 35): # testa se valor imc está entre 30(incluido) e 34.99 e imprime Obesidade grau 1
        print('Obesidade grau 1')
    elif(imc >= 35 and imc < 40): # testa se valor imc está entre 35(incluido) e 39.99 e imprime Obesidade grau 2
        print('Obesidade grau 2')
    elif(imc >= 40): # testa se valor imc está acima de 40(incluido) e imprime Obesidade grau 3 (obesidade mórbida)
        print('Obesidade grau 3 (obesidade mórbida)')

# print do titulo
print('--- Calculadora de IMC ---')
tipo_corpo(calcula_IMC())