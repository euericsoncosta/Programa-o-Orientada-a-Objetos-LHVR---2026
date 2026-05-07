

alunos = []


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    # aluno = {"nome": nome, "idade": idade}
    # alunos.append(aluno)
    alunos.append({"nome": nome, "idade": idade})


def listar_alunos():
    if not alunos:# Verifica se a lista de alunos está vazia, e estiver exibe a mensagem "Nenhum aluno cadastrado."
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}")

def exibir_menu():
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Sair")


def main():
    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            listar_alunos()
        elif opcao == 3:
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    main()