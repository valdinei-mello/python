"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separdor de casa decimaos na ´programação e o ponto e não a virgula
"""

# Errado do poto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# Certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

# É possivél fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para int
"""
OBS: Ao converter valores de float para int, nós perdemos precisão"""
resultado = int(valor)
print(resultado)
print(type(resultado))

# Podemos trabalhar com numeros complexos
variavel = 5j



