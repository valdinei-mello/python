"""
MAP

Com o map, fazemos mapeamento de valores para função.
------------------------------------

import math


def area(r):
    Calcula a área de um circulo
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]


# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - MAP
# MAP é uma função que recebe 2 parametros, o primeiro é a função e o segundo um iteravél. Retorna um MAP Object

areas = map(area, raios)
print(areas)


# Forma 3 - MAP com Lambda

calc = map(lambda x: x * 2, raios)
print(list(calc))

# OBS: após utilizar a função map(), depois da primeira utilização do resultado , ele zera.

# Para fixar  - Map

# Temos dados iteraveis:

# dados: a1, a2, ...., an

# Temos função:

# função: f(x)

# Utilizamos a função map(f,dados) onde map irá 'mapear', cada elemento dos dados e aplicar a função.

# O Map Object : f(a1), f(a2), ....., f(an)
"""

# Mais exemplos:

cidades = [('mococa', 28.86), ('campinas', 30), ('rio de janeiro', 39)]
print(cidades)

# f = 9 / 5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9 / 5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
