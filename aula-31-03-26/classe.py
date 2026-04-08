class Conta:#classe pai 
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def exibir_saldo(self):
        print(f"Saldo de {self.titular}: R${self.saldo:.2f}")

class ContaPoupanca(Conta): #classe filha que herda da classe pai (Conta)
    def __init__(self, titular, saldo, juros):
        # O super() traz o nome e o saldo do "pai" (Conta)
        super().__init__(titular, saldo)
        self.juros = juros  # Atributo exclusivo da filha

    def aplicar_juros(self):
        self.saldo += self.saldo * self.juros
        print(f"Juros aplicados! Novo saldo: R${self.saldo:.2f}")

class ContaCorrente(Conta): #classe filha que herda da classe pai (Conta)
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite  # Atributo exclusivo da filha

    def movimentacao(self): #valor descontado a cada movimentação
        self.saldo -= 5

    def sacar(self, valor):
        if self.saldo + self.limite >= valor: #verifica se o saldo mais o limite é suficiente para o saque
            self.movimentacao(self) #chama o método movimentação para descontar o valor da movimentação
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado! Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")
