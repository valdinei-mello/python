"""
Set Comprehension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}
"""

# Exemplos

numeros = {num for num in range(1, 10)}
print(numeros)

# Outros exemplos

numeros = {x ** 2 for x in range(10)}
print(numeros)

# OBS: Faça uma alteração na estrutura acima para gerar um dicionario ao inves de set
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Pra finalizar

letras = {letra for letra in 'valdinei'}
print(letras)

