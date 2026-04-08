class Conta_Bancaria:
    def __init__(self, numero_conta, titular):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = 0.0
    
    @property
    def numero_conta(self):
        return self.__numero_conta
    
    # @numero_conta.setter
    # def numero_conta(self, numero_conta):
    #     self.__numero_conta = numero_conta

    @property # decorator para indicar que o método é um getter, usado para acessar o valor do atributo privado
    def titular (self):
        return self.__titular
    
    @titular.setter # decorator para indicar que o método é um setter, usado para modificar o valor do atributo privado
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo
       

    def depositar(self, valor):
        self.__saldo +=valor
    

    
