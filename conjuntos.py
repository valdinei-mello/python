"""
COnjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a teoria dos cinjuntos da matematica

-Aqui os conuntos são chamados de Sets.

Dito isto da mesmo forma que na matematica:

    - Sets (conjuntos) não possuem valores duplicados;
    - Sets (conjuntos) não possuem valores ordenados;
    - Elementos não são acessados via indice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilixar quando precisamos armazenar elementos  mas não nos imortamos com a ordenação deles.
Quando não precisamos se precupar com chaves, valores e itens duplicados.

os conjuntos são referenciados em python com chaves{}

difetença entre conjuntos e mapas:
    - um dicionario tem chave e valor;
    - um conjunto tem apenas valor;

------------------------------------------
# Definindo um conjunto

# Forma 1:
# OBS: Ao criar um conjunto e tenha valor repetido ele irá ignorar

s = set({1, 2, 2, 3, 4, 4, 5, 6}) # Repare que temos valores repetidos
print(type(s))
print(s)

# Forma 2: MAis comun

s = {1, 2, 2, 3, 3, 4, 5, 6}
print(type(s))
print(s)
--------------------------------------

# Importante lembra que alem de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados
lista = [1, 1, 2, 3, 4, 4, 5, 8]
print(lista)

# Tuplas aceitam valores duplicados
tupla = 1, 1, 2, 3, 4, 4, 5, 8
print(tupla)

# Dicionario não aceita chaves duplicadas
dicionario = {}.fromkeys([1, 1, 2, 3, 4, 4, 5, 8], 'dict')
print(dicionario)

# Conjuntos não aceita valores duplcados
conjuntos = {1, 1, 2, 3, 4, 4, 5, 8}
print(conjuntos)
-------------------------------------------------

# Assim como todo outro conjunto python podemos colocar tipos de dados misturados em Sets
s = {1, 'e'}
print(s)

# Podemos interar em um set:
for valor in s:
    print(valor)
--------------------------------------------------------

# Usos interessantes com sets

# Imagine que fizemos um formalario de cadastro de vizitantes em uma feira ou museu e
# os visitantes informam manualmente a cidade de onde vieram.

# Nós adcionamos cada cidade em uma lista python, já que em uma lista podemos adicionar novos elementos e ter repetição

cidades = ['bh', 'sp', 'rj', 'rj', 'sp', 'mt']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantos cidades distintas, ou seja, unicas temos
# O que voce faria? Faria um loop na lista para verificar e tirar as repetições?
# Podemos usar o set para isto:

print(len(set(cidades)))
------------------------

# adicionando elementos em um conjunto
s = {1, 2, 3, 4}
s.add(5)
print(s)
------------------------------------------

# remover elementos em um conjunto
s = {1, 2, 3, 4}
print(s)

# Forma 1:
s.remove(2)
print(s)

# Forma 2:

s.discard(3)
print(s)
--------------------------------------------

# copiando um conjunto para outro
s = {1, 2, 3, 4}
print(s)

# forma 1: deep copy
novo_conj = s.copy()
print(novo_conj)

novo_conj.add(8)
print(novo_conj)
print(s)

# forma 2: shallow copy
print('--------------------------------------')
novo = s
print(s)
print(novo)

novo.add(12)
print(novo)
print(s)
-----------------------------------------------
# podemos remover todos os itens de um conjunto
s = {1, 2, 3, 4}
print(s)
s.clear()
print(s)
------------------------------------------

# metodos matematicos dos conjuntos

# imagine que temos 2 conjuntos:
# um contendo estudantes de python
# um contendo estudantes de java

estudantes_python = {'maria', 'ana', 'julia'}
estudantes_java = {'marcos', 'ana', 'paty', 'ney'}

# veja que alguns alunos estudam python e java.

# precisamos gerar um conjunto com nomes de estudantes unicos

# forma 1: utilizando union
unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)

# forma 2: utilizando o caracter pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# gerar um conjunto de estudante que estão em ambos os cursos

# forma 1: utilizando intersection
unicos3 = estudantes_java.intersection(estudantes_python)
print(unicos3)

# forma 2: utilizando o &
unicos4 = estudantes_python & estudantes_java
print(unicos4)

# gerar um conjunto de estudantes que fazem apenas um curso

unicos5 = estudantes_java.difference(estudantes_python)
print(unicos5)



"""


# soma, maior, minimo, tamanho
s = {1, 2, 3, 4}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

