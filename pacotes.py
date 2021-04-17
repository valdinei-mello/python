"""
Pacotes

Modulo = é apenas um arquivo python que pode ter diversas funções para utilizarmos.

Pacote = é um diretorio contendo uma coleção de modulos.

OBS: Não versões 2.x do python, um pacote python deveria conter dentrp dele um arquivo chamado __init__.py

Não versões do python 3.x, não é mais obrigátorio a utilização deste arquivo,
mas normalmente ainda é utilizado para manter compatibilidade.


================================

# Importando toda as funções do pacote

from geek import geek1, geek2
from geek.university import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(4, 8))

print(geek2.curso)
print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())


"""
# Importando apenas a função do arquivo

from geek.geek1 import funcao1
from geek.university.geek3 import funcao3

print(funcao1(2, 5))
print(funcao3())

