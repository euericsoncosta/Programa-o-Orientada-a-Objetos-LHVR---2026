class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.velocidade = 0
    
    def acelerar(self, valor):
        self.velocidade += valor
        print(f"O carro {self.modelo} acelerou para {self.velocidade} km/h.")

    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade <0:
            self.velocidade = 0
        print(f"O carro {self.modelo} freou para {self.velocidade} km/h.")