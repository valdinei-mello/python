"""
POO - Herança Multipla

Herança multipla, nada mais é do que a possibilidade de uma classe herdar de multiplas classes,
fazendo com que a classe filha herde todos os atributos e metodos de todos as classes herdadas.

OBS: A herança multipla, pode ser feito de duas maneiras:
    - Por multiderivação direta;
    - Por multiderivção indireta;


#  Exemplo 1: - multiderivação direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class Multiderivada(Base1, Base2, Base3):
    pass


#  Exemplo 2: - multiderivação indireta

class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3):
    pass

OBS: Não importa se a erivação é direta ou indireta. A classe que realizar a herança herdara
todos os atributos e metodos das super classes.

"""


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} esta nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} e estou nadando'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'O animal {self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


#  Testando

baleia = Aquatico('Willy')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Johw')
print(tatu.andar())
print(tatu.cumprimentar())

tux = Pinguim('Baby')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())  # ?????  Method Resolution Order - MRO


# Objeto é uma instancia de ...

print(f'Tux é uma instancia de Piguim? {isinstance(tux, Pinguim)} ')
print(f'Tux é uma instancia de Piguim? {isinstance(tux, Aquatico)} ')
print(f'Tux é uma instancia de Piguim?  {isinstance(tux, Terrestre)}')
print(f'Tux é uma instancia de Piguim? {isinstance(tux, object)} ')

