"""
REDUCE

OBS: apartir do python versão 3 a função redeuce() não é mais uma função integrada (bulti in).
Agora temos que importa e utilizar a função apartir do modulo 'functools'

Guido van Rossum: Utilize a função reduce() se voce realemente precise dela, Em todo caso,
99% das vezes um loop for é mais legivél

Para entender o reduce()

# Imagine que você tenha uma colção de dados:

dados = [a1, a2, a3,....]

# E você  tem uma função que recebe dosi parametros:

def função (x, y):
    return x + y

Assim como map() e filter(), a função reduce() recebe dois parametros: a função e o iteravél

    reduce(função, iteravel)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = fres1, a3) # Aplica a função passando o resultado do passo 1  + o terceiro elemenrtos e guarda o resultado.
    .
    .
    .
    Isso é repetido até o funal.

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce()irá retornar o resultado final.

Alternativamente, poderiamos ver a funçãi reduce(), como:

função (função(função(a1, a2)a3),a4)....))


"""

# Como funciona na pratica ?

# Vamos multiplicar todos os elemntos de uma lista

from functools import reduce

dados = [1, 2, 3, 5, 6, 8, 7]

# Para utilizar o redece() nósprecisamos de uma função que receba dosi parametros

mult = lambda x, y: x * y
resp = reduce(mult, dados)
print(resp)


# Utilizando um loop normal

x = 1
for n in dados:
    x = x * n

print(x)














