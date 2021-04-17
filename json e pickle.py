"""

JSON E PICKLE

JSON = Javascript Object Notation

API = São meios de comunicação entre os serviços oferecidos por empresas (facebook, youtube, ..)
e terceiros ( nós desenvolvedores).

================
import json

ret = json.dumps(['produtos', {'Playstation 4': ('2tb', 'novo', '220v', 2340)}])

print(type(ret))
print(ret)

================================
import json


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("TOM", "Angora")
print(felix.__dict__)

ret = json.dumps(felix.__dict__)
print(ret)

==================
Integrando o json com o pickle

pip install jsonpickle


import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("TOM", "Angora")
ret = json

==============================

# Escrevendo o arquivo jsonpickle

import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("TOM", "Angora")
with open('gato.json', 'w', encoding='utf-8') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)



"""

# Lendo o arquivo jsonpickle
from builtins import print

import jsonpickle


class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato("TOM", "Angora")
with open('gato.json', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)








