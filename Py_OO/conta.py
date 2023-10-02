class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print(f'Construindo objeto... {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo =  saldo
        self.__limite = limite
        
    def extrato(self):
        print(f'Saldo de {self.__saldo} da conta de titular {self.__titular}')
        
    def deposito(self, valor):
        self.__saldo += valor
        
    def saque(self, valor):
        self.__saldo -= valor
        
    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
        
