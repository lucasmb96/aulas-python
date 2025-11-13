
def tabuada():
    try:
        n = int(input("Digite um número para ver a tabuada: "))
        print(f"\n--- Tabuada do {n} ---")
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
        print("----------------------\n")
    except ValueError:
        print("Erro: insira um número válido.")


def calculadora():
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        print("\nOperações disponíveis:")
        print("[ 1 ] - Soma (+)")
        print("[ 2 ] - Subtração (-)")
        print("[ 3 ] - Multiplicação (*)")
        print("[ 4 ] - Divisão (/)")
        op = input("Escolha a operação: ")

        if op == "1":
            print(f"Resultado: {n1 + n2}")
        elif op == "2":
            print(f"Resultado: {n1 - n2}")
        elif op == "3":
            print(f"Resultado: {n1 * n2}")
        elif op == "4":
            if n2 == 0:
                print("Erro: divisão por zero não permitida.")
            else:
                print(f"Resultado: {n1 / n2}")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Erro: insira números válidos.")


def numpares():
    try:
        n = int(input("Digite um número: "))
        if n % 2 == 0:
            print(f"O número {n} é PAR.")
        else:
            print(f"O número {n} é ÍMPAR.")
    except ValueError:
        print("Erro: insira um número válido.")