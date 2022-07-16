class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(self.saldo)

    def saca(self, valor):
        self.saldo -= valor

    def deposita(self, valor):
        self.saldo += valor