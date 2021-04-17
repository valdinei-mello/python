"""
Pikcle


A função do pickle é realizar o segui te processo:

Objeto python = binarização
binarização = Objeto python

Este processo é chamado de serialização/deserialização

# OBS: O modulo picke não é seguto contra dados maliciosos e desta forma não é
recomendado trabalhar com arquivos pickle
vindos de outrso pessoas que você conheça ou de fontes deconhecidas.


"""

import pickle


class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome}, esta comendo ...')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome}, esta miando..')


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def latir(self):
        print(f'{self.nome}, esta latindo..')


# FAzendo a escrita em arquivo pickle


felix = Gato('Felix')
pluto = Cachorro("Pluto")

with open('animal.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)


# Fazer a leitura de dados em arquivo pickle

with open('animal.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.latir()



