from classe import Aluno
from banco import AlunoDAO


aluno = Aluno("José", 17, "Geografia")
alunos = AlunoDAO()
alunos.inserir(aluno)
lista_alunos = alunos.buscar_todos()
for aluno in lista_alunos:
    print(aluno)