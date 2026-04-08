


from classe import ContaPoupanca, ContaCorrente

contas = []

opc = 0

while opc != 5:
    print("Menu")
    print("1 - Criar Conta Poupança")
    print("2 - Criar Conta Corrente")  
    print("3 - Listar Contas e saldo")
    print("4 - Transferir dinheiro entre contas")
    print("5 - Sair")
    opc = int(input("Escolha uma opção: "))

    if opc == 1:
        titular = input("Digite o nome do titular: ")
        saldo = float(input("Digite o saldo inicial: "))
        juros = float(input("Digite a taxa de juros (em decimal): "))
        conta_poupanca = ContaPoupanca(titular, saldo, juros)
        contas.append(conta_poupanca)
        print("Conta Poupança criada com sucesso!")

    elif opc == 2:
        titular = input("Digite o nome do titular: ")
        saldo = float(input("Digite o saldo inicial: "))
        limite = float(input("Digite o limite de crédito: "))
        conta_corrente = ContaCorrente(titular, saldo, limite)
        contas.append(conta_corrente)
        print("Conta Corrente criada com sucesso!")
    
    elif opc == 3:
        for conta in contas:
            print(f"Titular: {conta.titular}, Saldo: R${conta.saldo:.2f}")

    elif opc == 4:
        nome_origem = input("Digite o nome do titular da conta de origem: ")
        nome_destino = input("Digite o nome do titular da conta de destino: ")
        valor = float(input("Digite o valor a ser transferido: "))

        conta_origem = next((conta for conta in contas if conta.titular == nome_origem), None)#next é uma função que retorna o primeiro item encontrado na lista que satisfaz a condição especificada, ou None se nenhum item for encontrado. Nesse caso, ele procura a conta de origem com base no nome do titular fornecido pelo usuário. pega a refrencia na memoria e salva na variavel conta_origem, para que possa ser manipulada posteriormente. 
        conta_destino = next((conta for conta in contas if conta.titular == nome_destino), None)#next é uma função que retorna o primeiro item encontrado na lista que satisfaz a condição especificada, ou None se nenhum item for encontrado. Nesse caso, ele procura a conta de destino com base no nome do titular fornecido pelo usuário.

        if conta_origem and conta_destino:
            if conta_origem.saldo >= valor:
                conta_origem.saldo -= valor
                conta_destino.saldo += valor
                print("Transferência realizada com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Uma ou ambas as contas não foram encontradas.")

    else:
        print("Opção inválida. Tente novamente.")