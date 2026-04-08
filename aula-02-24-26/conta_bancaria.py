class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor} realizado. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo}")