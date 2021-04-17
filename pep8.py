"""
PEP8 - Python Enhancement Proposal

São proposta de melhorias para a linguagem Python

Zen off Python

import this

A ideia da PEP8 é que possamos ecrever codigos python de forma pythonica.

[1]-Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass


[2]-Utilize nomes minusculo, separados por underline para funções ou variaveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4


numero_impar = 3

[3]-Utilize 4 espaços para identação!(NÃO USE TAB)

if 'a' in 'banana':
    print("tem")

[4]-Linhas em branco
-Separa funções e definições de classe com duas linhas em branco;
-Metodos dentro uma classe deve ser separados com uma unica linha em branco;

[5]-Imports
-Imports devem ser sempre feitos em linhas separadas;

#Import Errado

import sys, os

#Import Certo

import  sys
import  os

#Não há proble em utilizar :

from types import StringType,LisType

#Caso tenha muitos imports do mesmo pacote, recomenda-se fazer:

from types import(
    StringType,
    ListType

)

#Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrins e
# antes de cnstantes e variaveis globais.

[6]-Espaços em expressões e instruções

#Não faça:

funcao( algo[ 1 ])

#Faça:

funcao(algo[1])

#Não faça:

algo (1)

#Faça:

#algo(1)

#Não faça:

dict ['chave'] = list [indice]

#Faça:

dict['chave'] = list[indice]

#Não faça:

x        = 1
y        = 2
variavel = 3

#Faça:

x = 1
y = 2
variavel = 3

[7]-Termine sempre uma instruçã sempre com uma nova linha
"""
import this
