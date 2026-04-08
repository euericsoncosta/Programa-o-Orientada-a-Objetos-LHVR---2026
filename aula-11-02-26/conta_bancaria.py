class ContaBancaria:
    

    def __init__(self, titular, saldo_inicial, numero_da_conta):
        self.titular = titular
        self.saldo = saldo_inicial
        self.numero_da_conta = numero_da_conta
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")
    
    def sacar(self, valor):
        
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")
      