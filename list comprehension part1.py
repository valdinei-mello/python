"""
List Comprehension part 1

 - utilizando list comprehension nós podemos gerar novas lista com dados processados apartir de outro iteravel.

# Sintaxe da List Comprehension

[dado for dado in iteravel]
--------------------------------------------

# Exemplos

numeros = [1, 2, 3, 4, 5, 6]

res = [numero * 10 for numero in numeros]
print(res)


Para intender melhor o que esta acontecendo devemos dividir a expressão em duas partes:
    - A primeira parte: for numero in numeros
    - A segunda parte: numero * 10

res = [numero / 2 for numero in numeros]
print(res)


def quadrado(valor):
    return valor * valor


res = [quadrado(numero) for numero in numeros]
print(res)
------------------------------------

# List Comprehension versus Loop

# Loop
numero_dobrados = []
for num in [1, 2, 3, 4, 5]:
    numero_dobrados.append(num * 2)

print(numero_dobrados)

# List Comprenhension
print([numero * 2 for numero in[1, 2, 3, 4, 5]])

"""


# Outros Exemplos
# 1
nome = "valdinei de mello"

print([letra.upper()for letra in nome])

# 2
amigos = ["maria", "julia", "pedro", "marcos"]

print([amigo.title() for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])


