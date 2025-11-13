def calcula_media(valores):
    soma = 0
    for numero in valores:
        soma += valores
    
    media = soma / len(valores)

    print(f'A media é: {media:.2f} valores.')

lista = [10, 10, 10, 10]

calcula_media(lista)

def main():
    programa(mostra_menu())

if __name__ == '__main__':
    main()