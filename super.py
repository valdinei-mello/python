"""
POO - Método super()

O método super() se refere a super classe.


"""


class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'Este animal fala {som}')


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca


tom = Gato('tom', 'felino', 'algora')

print(tom.__dict__)
tom.faz_som('miau')

