# Biblioteca (Livro): título, autor, ano de publicação, gênero.

class Livro:
    def __init__(self, titlo, autor, ano_publicacao, genero, id = None):
        self.id = id
        self.titulo = titlo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

    def __str__(self):
        return f"ID: {self.id} | Título: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao} | Gênero: {self.genero}"
