import os
from datetime import datetime

os.system('cls')

cliente = dict()
ano_atual = datetime.now().year

cliente['nome'] = input('Digite o seu nome: ')
cliente['ano_nascimento'] = int(input('Digite o seu ano de nascimento: '))
cliente['rendimentos_mensais'] = float(input('Digite os seus rendimentos mensais: '))
cliente['despesas_mensais'] = float(input('Digite o montante de despesas mensais: '))
cliente['montante_credito'] = float(input('Digite o montante de credito: '))
cliente['prazo'] = int(input('Digite o prazo em anos: '))

cliente['idade'] = ano_atual - cliente['ano_nascimento']
cliente['remanescente'] = cliente['rendimentos_mensais'] - cliente['despesas_mensais']
cliente['mensalidade'] = cliente['montante_credito'] / (cliente['prazo'] * 12)
cliente['situacao'] = 'Aprovado' if cliente['remanescente'] > cliente['mensalidade'] else 'Reprovado'

print(cliente['situacao'])