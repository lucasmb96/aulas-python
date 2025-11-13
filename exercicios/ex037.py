import os

os.system('cls')

try:
    num1= int(input("Digite um número: "))
    num2= int(input("Digite outro número: "))
    div = num1/num2
except ZeroDivisionError:
    print("Outro numero não pode ser zero")
except ValueError:
    print("Número não é valido")
else:
    print(f'A divisão é {div}')

    