"""
Dictionay_ Comprehension

Pensando no seguinte:

-Se quisermos criar uma lista, fazemos:

lista = [1, 2 , 3, 4]

-Se quisermos criar uma tupla:

tupla = (1, 2 , 3, 4) # tupla = 1, 2 , 3, 4

- Se quisermos criar um conjunto:

conjunto = {1, 2 , 3, 4}

-Se quisermos criar um dicionario:

dicionario = {'a:1, 'b':2, 'c':3, 'd':4}

# SINTAXE:

{chave:valor for valor in iteravél}  # Dictionaty Comprehension
[valor for valor in iteravel]  # List Comprehension
--------------------------------------------------------

# Exemplos:

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)
----------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)
--------------------------------------------------

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
---------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7]
resp = {num: ('par' if num % 2 == 0 else 'impar')for num in numeros}
print(resp)

"""





