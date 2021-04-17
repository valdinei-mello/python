"""
POO - MRO = Method Resolution Order

Method Resolution Order (Resolução de ordem de método) é a ordem de execução dos metodos,
 .ou seja, quem será executado primeiro.

 Em pyhton a gente pode ocnferir a ordem de execuçã dos métodso de 3 formas:
    - Via propriedade da classe __mro__;
    - Via método;
    - Via help;
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


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


#  Testando


tux = Pinguim('Baby')
print(tux.cumprimentar())  # ?????  Method Resolution Order - MRO

"""
Pinguim(Aquatico, Terrestre):
Eu sou Baby e estou nadando


class Pinguim( Terrestre, Aquatico):
Eu sou Baby da terra
"""