"""
Generators Expression

Em aulas anteriores nós estudamos:
    - List Comprehension;
    - Dictionary Comprehension;
    - Set Comprehension;

Não vimos:
- Tuplas Comprehension..... porque elas se chamam Generators

nomes = ['carlos', 'camila', 'cathia', 'casiano']
printy(any([nome[0] == 'c' for nome in nomes])
-----------------------------------------------

# Poderiamos ter feito utilizando generators

nomes = ['carlos', 'camila', 'cathia', 'casiano']
print(any(nome[0] == 'c' for nome in nomes))

# List Comprehension
resp = [nome[0] == 'c' for nome in nomes]
print(type(resp))
print(resp)

# Genarator
resp = (nome[0] == 'c' for nome in nomes)
print(type(resp))
print(resp)

------------------------------------

# Qual é a utilidade de getsizeof()? Retorna a qtde de bytes em memoria do elemnto passado como parametro

from sys import getsizeof

# Mostra a qtde de bytes a string esta ocupando em memória, e quanto maior a string mais espaço ela irá ocupar

print(getsizeof('vadinei'))
print(getsizeof("valdinei de mello"))

"""

from sys import getsizeof

# Gerando uma lista de numero, com list comprehension
list_comp = [x * 10 for x in range(1000)]
print(getsizeof(list_comp))


# Gerando uma lista de numero, com set comprehension
set_comp = {x * 10 for x in range(1000)}
print(getsizeof(set_comp))


# Gerando uma lista de numero, com dictionary comprehension
dic_comp = ({x: x * 10 for x in range(1000)})
print(getsizeof(dic_comp))


# Gerando uma lista de numero com generator
ger = (x * 10 for x in range(1000))
print(getsizeof(ger))


# Eu posso iterar no generator expression ? sim
ger = (x * 10 for x in range(1000))
print(ger)
print(type(ger))

for n in ger:
    print(n)

