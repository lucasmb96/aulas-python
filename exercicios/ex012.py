nome = input('nome:').strip()
nome = nome.rsplit()
print('Olá', nome[0] +', o seu registo está completo!')

print('O seu mail é:',nome[0][0].lower()+'.'+ nome[1].lower()+'@empresa.pt')
