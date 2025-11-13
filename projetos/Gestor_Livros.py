import os
from pathlib import Path

os.system('cls')


ficheiro = Path('livros.txt')


def carregar_livros():
    # Lê os livros do ficheiro e devolve uma lista
    livros = [] # lista vazia para preencher do ficheiro
    if ficheiro.exists(): # verifica se existe ficheiro
        with ficheiro.open('r', encoding='utf-8', errors='ignore') as f:
            for linha in f: # leitura das linhas do ficheiro
                titulo, autor, lido = linha.strip().split(';') # remove espaços e ponto e virgula
                livros.append({ # adiciona a um dicionario as variaveis
                    'titulo': titulo,
                    'autor': autor,
                    'lido': lido == 'True'
                })
    else:
        # Cria o ficheiro vazio se não existir
        with ficheiro.open('w', encoding='utf-8', errors='ignore'):
            pass
    return livros


def guardar_livros(livros):
    # Guarda a lista de livros no ficheiro.
    with ficheiro.open('w', encoding='utf-8', errors='ignore') as f:
        for livro in livros:
            f.write(f"{livro['titulo']};{livro['autor']};{livro['lido']}\n")


def adicionar_livro(livros):
    # Pede informação sobre o livro e chama função que insere no ficheiro
    titulo = input("Título: ")
    autor = input("Autor: ")
    livros.append({'titulo': titulo, 'autor': autor, 'lido': False})
    guardar_livros(livros) # Chama função guardar_livros para guardar no ficheiro
    print(f'Livro "{titulo}" adicionado com sucesso!')


def marcar_lido(livros, lido=True):
    # Pede titulo do livro e altera parametro lido
    titulo = input("Título do livro: ")
    for livro in livros:
        if livro['titulo'].lower() == titulo.lower():
            livro['lido'] = lido
            guardar_livros(livros)
            print(f'O livro "{titulo}" foi marcado como {"Lido" if livro["lido"] else "Não lido"}.')
            return
    print("Livro não encontrado.")


def mostrar_todos(livros):
    # Mostra todos os livros do ficheiro
    if livros == []:
        print("Nenhum livro registado.")
    else:
        for livro in livros:
            estado = "Lido" if livro['lido'] else "Não lido"
            print(f"{livro['titulo']} - {livro['autor']} ({estado})")


def mostrar_lidos(livros):
    # Mostra todos os livros lidos do ficheiro
    lidos = [l for l in livros if l['lido']]
    if lidos == []:
        print("Nenhum livro lido.")
    else:
        for l in lidos:
            print(f"{l['titulo']} - {l['autor']} (Lido)")


def mostrar_nao_lidos(livros):
    # Mostra todos os livros não lidos do ficheiro
    nao_lidos = []
    for l in livros:
        if l['lido'] == False:
            nao_lidos.append(l)
    if nao_lidos == []:
        print("Não existe livros não lidos")
    else:
        for l in nao_lidos:
            print(f"{l['titulo']} - {l['autor']} (Não lido)")


livros = carregar_livros()

while True: # ciclo while até á escolha 0 para Sair
    print("\n--- GESTOR DE LIVROS ---")
    print("1. Adicionar livro")
    print("2. Marcar livro como lido")
    print("3. Marcar livro como não lido")
    print("4. Mostrar todos os livros")
    print("5. Mostrar apenas livros lidos")
    print("6. Mostrar apenas livros não lidos")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_livro(livros)
    elif opcao == "2":
        marcar_lido(livros, True)
    elif opcao == "3":
        marcar_lido(livros, False)
    elif opcao == "4":
        mostrar_todos(livros)
    elif opcao == "5":
        mostrar_lidos(livros)
    elif opcao == "6":
        mostrar_nao_lidos(livros)
    elif opcao == "0":
        print("A sair...")
        break
    else:
        print("Opção inválida. Tente novamente.")