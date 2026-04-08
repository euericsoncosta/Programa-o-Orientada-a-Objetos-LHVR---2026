# Importamos as classes que criamos no outro arquivo
from modelos import Aluno, AlunoDAO

def exibir_menu():
    print("\n" + "="*30)
    print(" SISTEMA DE GESTÃO DE ALUNOS ")
    print("="*30)
    print("1. Adicionar novo aluno")
    print("2. Listar todos os alunos")
    print("3. Atualizar um aluno")
    print("4. Deletar um aluno")
    print("0. Sair do programa")
    print("="*30)

def main():
    # Instanciamos o DAO uma única vez para usar em todo o programa
    dao = AlunoDAO('escola_interativa.db')

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n--- ADICIONAR ALUNO ---")
            nome = input("Nome do aluno: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")
            
            # Criamos o objeto Aluno (sem ID, pois o banco vai gerar)
            novo_aluno = Aluno(nome, idade, curso)
            # Passamos o objeto para o DAO salvar
            dao.inserir(novo_aluno)

        elif opcao == '2':
            print("\n--- LISTA DE ALUNOS ---")
            alunos = dao.buscar_todos()
            
            if not alunos:
                print("Nenhum aluno cadastrado no momento.")
            else:
                for aluno in alunos:
                    print(aluno)

        elif opcao == '3':
            print("\n--- ATUALIZAR ALUNO ---")
            id_aluno = int(input("Digite o ID do aluno que deseja atualizar: "))
            nome = input("Novo nome: ")
            idade = int(input("Nova idade: "))
            curso = input("Novo curso: ")
            
            # Criamos o objeto já com o ID, para o DAO saber quem atualizar
            aluno_atualizado = Aluno(nome, idade, curso, id_aluno)
            dao.atualizar(aluno_atualizado)

        elif opcao == '4':
            print("\n--- DELETAR ALUNO ---")
            id_aluno = int(input("Digite o ID do aluno que deseja deletar: "))
            dao.deletar(id_aluno)

        elif opcao == '0':
            print("\nSaindo do sistema... Até logo!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

# Garante que o menu só inicie se este arquivo for executado diretamente
if __name__ == '__main__':
    main()