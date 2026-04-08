


#usando atributos de classe

class ContaBancaria:
    numero_conta = 0
    def __init__(self, titular):
        ContaBancaria.numero_conta +=1
        self.numero_conta = ContaBancaria.numero_conta
        self.titular = titular

    def __str__(self):
        return f"Titular:{self.titular}, Número da conta: {self.numero_conta}"


