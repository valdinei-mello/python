"""
funções com retorno

numeros = [1, 2, 3, 4]

ret = numeros.pop()
print(f'retorno de POP: {ret}')

ret1 = print(numeros)
print(ret1)


OBS: em python quando uma função nao retorna nenum valor o retorno é NONE;
OBS: funções python que retorne valores deve retornar estes valores com a palavra RETURN;
OBS: não precisamos necessariamente criar uma variavel para receber o retorno de uma função. podemos passar
a execução da função para outras funções;

# Vamos refatorar esta função para que ela retorne um valor

def quadrado_de_7():
    return 7*7

# criamos uma variavel para recebermos o retrono da função
ret = quadrado_de_7()
print(ret)

print(quadrado_de_7() + 1)
------------------------

# refatorando a primeira função

def diz_oi():
    return 'oi '

alguem = 'pedro'
print(diz_oi() + alguem)

OBS: sobre a palavra return:
    1 - ela finaliza a função, ouseja, ela sai da execução da função;
    2 - podemos ter em uma função, diferentes returns;
    3 - podemos em uma função retornar qualquer tipo de dado e ate mesmo multiplos valores;

# exemplos 1: ela finaliza a função, ouseja, ela sai da execução da função;

def diz_oi():
    print('estou sendo executado antes do retorno...')
    return 'olá ney'
    print('estou sendo executado apos o retorno')

print(diz_oi())
------------------------------------------

# exemplo 2: podemos ter em uma função, diferentes returns;

def nova_função():
    variavel = None
    if variavel:
        return 4
    elif variavel is None:
        return 3.4
    return 'asd'

print(nova_função())
-----------------------

# exemplo 3:

def outra_função(): podemos em uma função retornar qualquer tipo de dado e ate mesmo multiplos valores;
    return 2, 3, 4, 5

# num1, num2, num3, num4 = outra_função()
# print(num1, num2, num3, num4)

print(outra_função())
---------------------------------

# vamos criar uma função para jogar moeda

from random import random


def jogar_moeada():
    # gera um numero pseudo-randomico entre '0 e 1'
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(jogar_moeada())



"""

# erros comuns na utilização do retorno de uma função


def impar():
    numero = 8
    if numero % 2 != 0:
        return True
    else:  # Linha desnecessaria, pois se não é TRUE so restará FALSE
        return False


print(impar())

