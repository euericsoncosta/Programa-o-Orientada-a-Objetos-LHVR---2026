class Aluno:
    def __init__(self, nome, idade, curso, id_aluno = None):
        self.id = id_aluno
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Idade: {self.idade} | Curso: {self.curso}"
    