import os

os.system('cls')

def converter(temp):
    f = (temp * 9/5) + 32
    print(f'{temp}°C celsius são {f:.2f}°F fahrenheit')


converter(float(input('Digite a temperatura a ser convertida: ')))