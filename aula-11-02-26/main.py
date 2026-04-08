from veiculo import Carro       #importando a classe Carro do arquivo veiculo.py

modelo = input("Digite o modelo do carro: ")
carro1 = Carro(modelo)

opc = 0
while opc != 3:
    print("1 - Acelerar")
    print("2 - Frear")
    print("3 - Sair")
    opc = int(input("Escolha uma opção: "))
    if opc == 1:
        valor = int(input("Digite o valor para acelerar: "))
        carro1.acelerar(valor)
    elif opc == 2:
        valor = int(input("Digite o valor para frear: "))
        carro1.frear(valor)
    else:
        print("Saindo do programa...")