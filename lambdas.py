"""
Utilizando Lambdas

Conhecidas por expressões lambdas ou simplismente lambdas, são funções sem nome, ou seja, funções anonimas.

--------------------------
# Função em python

def função(x):
    return x * 3 + 1


print(função(4))


# Expressão lambda

lambda x: 3 * x + 1

# Como utilizar a expressão lambda ?

calc = lambda x: 3 * x + 1
print(calc(4))
--------------------------------


# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('  valdinei  ', ' mello'))

----------------------------------------
# Em funções python, podemos ter nenhuma ou varias entradas. Em labda tambem

amor = lambda: 'Como não amar python'

print(amor())
-------------------------------------------

# Outro exemplo

autores = ['jorge lucas', 'marcos c. lima', 'matheus souza', 'ana clara da luz', 'caio']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())
print(autores)

"""


# Função quadratica

# f(x) = a * x ** 2 + b * x + c


# Definindo a função

def geradora_função_quadratica(a, b, c):
    """
    Retorna a função de x: f(x) = a * x ** 2 + b * x + c
   """
    return lambda x: a * x ** 2 + b * x + c


print(geradora_função_quadratica(4, 2, 8)(4))

