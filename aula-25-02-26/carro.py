# Atividade 2: Sistema de Controle de Combustível
# Objetivo: Criar uma classe que simule o painel de um veículo, controlando o nível de
# combustível enquanto ele "viaja".
# Requisitos:
# 1. Classe: Carro
# 2. Atributos:
# o modelo (String)
# o tanque (Número, capacidade atual de litros)
# o consumo (Número, quantos km o carro faz por litro)
# 3. Métodos:
# o abastecer(litros): Adiciona combustível ao tanque.
# o viajar(distancia): Calcula quantos litros serão necessários para percorrer a
# distância.
#  Se tiver combustível: subtrai do tanque e exibe "Viagem concluída".
#  Se não tiver: exibe "Combustível insuficiente para esta distância".
# o status(): Exibe o modelo do carro e quantos litros restam no tanque.

class Carro:
    def __init__(self, modelo, consumo):
        self.modelo = modelo
        self.tanque = 0
        self.consumo = consumo

    def abastecer(self, litros):
        self.tanque += litros
        print(f"{litros} litros adicionados ao tanque. Total: {self.tanque} litros.")

    def viajar(self, distancia):
        litros_necessarios = distancia / self.consumo
        if self.tanque >= litros_necessarios:
            self.tanque -= litros_necessarios
            print("Viagem concluída.")
        else:
            print("Combustível insuficiente para esta distância.")

    def status(self):
        print(f"Modelo: {self.modelo}")
        print(f"Litros restantes no tanque: {self.tanque:.2f} litros.")