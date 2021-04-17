"""
POO - Propriedades - Properties

Em linguagem de proramação com o Java , ao declararmos os atributos  privados nas classes, costumamos  a criar
métodos publicos para manipulação desses atributos. Esses métodos são conhecidos por getters e setteres, onde os
getteres retornam o valor do atributo e o setters alteram o valor do mesmo.

==========================================

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
        self.__numero = Conta.contador

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limte(self, limite):
        self.__limite = limite


conta1 = Conta('valdinei', 2140.00, 10.00)
conta2 = Conta('jorge', 2100.00, 2145.00)


print(conta1.extrato())
print(conta2.extrato())


soma = conta1.get_saldo() + conta2.get_saldo()
print(f'A soma do saldo das contas é {soma}')

print(conta1.get_limite())
conta1.set_limte(1000.00)
print(conta1.get_limite())

=============
"""


class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
        self.__numero = Conta.contador

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__limite + self.__saldo


conta1 = Conta('valdinei', 2140.00, 10.00)
conta2 = Conta('jorge', 2100.00, 2145.00)

print(conta1.extrato())
print(conta2.extrato())


soma = conta1.saldo + conta2.saldo
print(f'A soma do saldo das contas é {soma}')

print(conta1.__dict__)
conta1.limite = 58471
print(conta1.__dict__)
print(conta1.limite)
print(conta1.valor_total)

