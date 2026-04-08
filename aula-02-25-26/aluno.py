class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.notas = []

    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            print("Nenhuma nota registrada.")
        else:
            media = sum(self.notas)/ len(self.notas)
            print(f"A média de {self.nome} é: {media:.2f}")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Curso: {self.curso}")
        print(f"Notas: {self.notas}")


