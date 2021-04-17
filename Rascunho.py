"""

Rascunho para estudo
"""


class Animal:
    def __init__(self, nome, raca, cor):
        self.__nome = nome
        self.__raca = raca
        self.__cor = cor

    def __repr__(self):
        return f'{self.__nome}, {self.__cor}, {self.__raca}'


class Cachorro(Animal):
    def __init__(self, nome, raca, cor, porte):
        super().__init__(nome, raca, cor)
        self.__porte = porte

    def __repr__(self):
        return f'{self._Animal__nome}, {self._Animal__raca}, {self._Animal__cor}, {self.__porte}'


ave = Animal("louro josé", "papagaio", "verde")
print(ave)


pluto = Cachorro("Pluto", "vira-lata", "preto", "pequeno")

print(pluto)

