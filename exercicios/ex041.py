class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    

    def descricao(self):
        print(f'O livro com o tiulo {self.titulo} foi escrito pelo autor {self.autor}.')


livro1 = Livro('qwerty', '123')
livro2 = Livro('azerty', '123')
livro3 = Livro('omerty', '321')

livro1.descricao()
livro2.descricao()
livro3.descricao()

