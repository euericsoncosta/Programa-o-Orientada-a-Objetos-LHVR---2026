from aluno import Aluno
alunos = []
opc = 0

while opc != 5:
    print("1 - Cadastrar aluno")
    print("2 - Adicionar nota")
    print("3 - Exibir informações do aluno")
    print("4 - listar alunos")
    print("5 - Sair")
    opc = int(input("Escolha uma opção: "))

    if opc == 1:
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ")
        # alunos.append(Aluno(nome, idade, curso))
        alu = Aluno(nome, idade, curso)
        alunos.append(alu)
    elif opc == 2:
        nome = input("Digite o nome do aluno: ")
        nota = int(input("Digite a nota do aluno: "))
        for alu in alunos:
            if alu.nome == nome:
                alu.adicionar_nota(nota)
                break
    elif opc == 3:
        nome = input("Digite o nome do aluno: ")
        for alu in alunos:
            if alu.nome == nome:
                alu.exibir_informacoes()
                alu.calcular_media()
                break

    elif opc == 4:
        for alu in alunos:
            print(f"Nome: {alu.nome} - Curso: {alu.curso}")

    elif opc == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")
    


