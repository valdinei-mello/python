"""
POO - Polimorfismo

Poli = Muitas
Morfis = Formas



"""


class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método ')

    def comer(self):
        print(f'{self.__nome} está comendo')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')


class Gata(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} diz miau')


class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} diz algo ...')


felix = Gata('felix')
felix.comer()
felix.falar()

pluto = Cachorro('Pluto')
pluto.comer()
pluto.falar()

mikey = Rato('Mikey')
mikey.comer()
mikey.falar()
