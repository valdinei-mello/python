"""
modulo collections - named tuple

# recapitulando tupla
tupla = (1, 2, 3, 4)
print(tupla[1])
--------------------------------

# named_tupla = são tuplas diferenciadas onde especificamos um nome para a mesma e tbm parametros.

"""

# importando
from  collections import namedtuple

# precisamos definir o nome e parametros

# forma 1: declaração named tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2: declaração maed tuple
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# forma 3: declaração named tupla
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# usando
ray = cachorro(idade=2, raca='viralata', nome='bili')
print(ray)

# acessando os dados:

# forma 1:
print(ray[0])  # idade
print(ray[1])  # raça
print(ray[2])  # nome

# forma 2:
print(ray.idade)  # idade
print(ray.raca)  # raça
print(ray.nome)  # nome

print(ray.index('viralata'))
print(ray.count('viralata'))
