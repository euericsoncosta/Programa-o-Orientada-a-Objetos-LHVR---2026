# from conta_bancaria import ContaBancaria # Importação da classe ContaBancaria do módulo conta_bancaria
from conta_bancaria import * # Importação de todas as classes e funções do módulo conta_bancaria

titular = input("Digite o nome do titular da conta: ") # Solicita ao usuário o nome do titular da conta
conta = ContaBancaria(titular)

opc = 0

while opc != 4: 
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Exibir Saldo")
    print("4 - Sair")

    opc = int(input("Escolha uma opção: "))

    if opc == 1:
        valor = float(input("Digite o valor para depositar:"))
        conta.depositar(valor)

    elif opc == 2:
        valor = float(input("Digite o valor para sacar:"))
        conta.sacar(valor)

    elif opc == 3:
        conta.exibir_saldo()
    elif opc == 4:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")