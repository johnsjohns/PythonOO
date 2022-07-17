class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(self.__saldo)

    def saca(self, valor):
        self.__saldo -= valor

    def deposita(self, valor):
        self.__saldo += valor

    def tranfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
