"""
Tipo Booleano

Algebra Booleana, criado por George Boole

2 coonstantes: Verdadeiro, Falso

Verdadeiro = True
Falso = False

OBS: Sempre com inicial MAIUSCULA

Errado:

true, false

Certo:

True, False
"""

ativo = True
print(ativo)

"""
Operações basicas:
"""

# Negação (not):
"""
Fazendo com que o resultado se inverta 
"""
print(not ativo)
logado = False

# Ou (or):
"""
É uma operação binaria, ou seja, um dos dois valores precisa ser verdadeira

True or False = True
False or True = True
True or True = True
False or False = False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binaria, e ambos os valores precisam ser verdadeiros

True or False = False
False or True = False
True or True = True
False or False = False
"""
print(ativo and logado)