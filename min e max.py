"""
Min e Max

max() = retorna o maior valor em um iteravel ou maior entre dois ou mais elementos

# Exemplos

lista = [1, 8, 3, 55]
print(max(lista))

tupla = (1, 8, 3, 55)
print(max(tupla))

conjunto = {1, 8, 3, 55}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 3, 'd': 55}
print(max(dicionario.values()))
-----------------------------------------

# FAça um programa que receba dois valorrs e mostre o maior

val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
print(max(val1, val2))
-------------------

print(max(4, 2, 3))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'd'))
print(max(1.47, 1.74))
print(max('valdinei de mello'))
-------------------------------------------------------------
--------------------------------------------------------------

min() = retorna o menor valor em um iteravel ou menor entre dois ou mais elementos

# Exemplos

lista = [1, 8, 3, 55]
print(min(lista))

tupla = (1, 8, 3, 55)
print(min(tupla))

conjunto = {1, 8, 3, 55}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 3, 'd': 55}
print(min(dicionario.values()))
-----------------------------------------

# FAça um programa que receba dois valorrs e mostre o menor

val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
print(min(val1, val2))
-------------------

print(min(4, 2, 3))
print(min('a', 'ab', 'abc'))
print(min('a', 'b', 'c', 'd'))
print(min(1.47, 1.74))
print(min('valdinei de mello'))
-----------------------------------


# Outros exemplos

nomes = ['caio', 'ana', 'marcos', 'jorge', 'julio', 'mauricio', 'obama', 'trump']
print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))


"""

musicas = [
    {'titulo': 'acdc', 'tocou': 3},
    {'titulo': 'iron', 'tocou': 10},
    {'titulo': 'ramones', 'tocou': 8},
    {'titulo': 'metalica', 'tocou': 13},
    {'titulo': 'calypso', 'tocou': 1}
]


print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))


# DESAFIO! Imprima somente o titulo da musica mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])


# DESAFIO! Como encontrar a musica mais e a menos tocada, sem usa max(), min() e lambda

max = 0
min = 100


for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica_max in musicas:
    if musica_max['tocou'] == max:
        print(musica_max['titulo'])

for musica_min in musicas:
    if musica_min['tocou'] == min:
        print(musica_min['titulo'])
