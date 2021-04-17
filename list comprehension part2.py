"""
List Comprehension Part2


Nós podemos add estruturas condicionais logicas as nossas list comprehension
"""

# Exemplos 1:

lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)

pares = [numero for numero in lista if numero % 2 == 0]
print(pares)

impares = [numero for numero in lista if numero % 2 != 0]
print(impares)


# Refatorar

# OBS: Qualquer numero par modulo 2 é 0 e 0 em python é FALSO, not false = True
pares = [numero for numero in lista if not numero % 2]

# OBS: Qualquer numero impar modulo 2 é 1, e 1 em python é TRUE
impar = [numero for numero in lista if numero % 2]

print(pares)
print(impares)


# Exemplo 2:

resp = [numero * 2
        if numero % 2 == 0
        else numero / 2
        for numero in lista]
print(resp)

