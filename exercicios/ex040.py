class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    

livro1 = Livro('qwerty', '123')
livro2 = Livro('azerty', '123')
livro3 = Livro('omerty', '321')

print(f'Titulo: {livro1.titulo} do autor: {livro1.autor}')
print(f'Titulo: {livro2.titulo} do autor: {livro2.autor}')
print(f'Titulo: {livro3.titulo} do autor: {livro3.autor}')