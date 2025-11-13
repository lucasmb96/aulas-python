#Importação da biblioteca
import time

def calcular_arearetangulo(largura, altura):
    """"Calcula a área de um retabgulo."""
    return largura * altura

#Código principal
largura = 5
altura = 3

#Chamada da função para calcular a área
area = calcular_arearetangulo(largura, altura)

#Imprimir resultado
time.sleep(1)
print(f"A área do retangulo é {area}")
