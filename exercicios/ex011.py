frase = input('frase: ').strip()

frase = frase.lower()
print(int(frase.count('a')))

print(frase.find('a')+1)

print(frase.rfind('a')+1)