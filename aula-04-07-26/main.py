from classe import Aluno
from banco import AlunoDAO


# aluno = Aluno("José", 17, "Geografia")
# alunos = AlunoDAO()
# alunos.inserir(aluno)
# lista_alunos = alunos.buscar_todos()
# for aluno in lista_alunos:
#     print(aluno)


def exibir_menu():
    print("-" * 30)
    print("SISTEMA DE GESTÃO DE ALUNOS")
    print("-" * 30)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Atualizar aluno")
    print("4 - Deletar aluno")
    print("0 - Sair")
    print("-" * 30)

def main():
    alunos = AlunoDAO()
    while True:
        exibir_menu()
        opcao = int(input("Digite a opcao desejada: "))

        if opcao == 1:
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            curso = input("Digite o curso do aluno: ")
            aluno = Aluno(nome, idade, curso)
            alunos.inserir(aluno)

        elif opcao == 2:
            lista_aluno = alunos.buscar_todos()
            for aluno in lista_aluno:
                print(aluno)
            
        elif opcao == 3:
            id_aluno = int(input("Digite o ID do aluno a ser atualizado: "))
            nome = input("Digite o novo nome do aluno: ")
            idade = int(input("Digite a nova idade do aluno: "))
            curso = input("Digite o novo curso do aluno: ")
            aluno = Aluno(nome, idade, curso, id_aluno)
            alunos.atualizar(aluno)

        elif opcao == 4:
            id_aluno = int(input("Digite o ID do aluno a ser deletado: "))
            alunos.deletar(id_aluno)

        elif opcao == 0:
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
