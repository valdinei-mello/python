"""
LISTAS (list)

Listas em python funcionan com vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINAMICO e tambem de podermos colocar QUALQUER tipo de dados.

Linguagens C/JAVA:
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se voce criar um array do tipo int e com tamanho 5, este array
    será sempre do tip inteiro e podera ter sempre no maximo 5 valores.

Já em Python:
- Dinâmico: Não possui tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adcionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo dado

As lista em Python são representadas por colchetes: []
Listas são mutaveis, ou seja, elas podem mudar constantemente

type([])

lista1 = [1, 2, 12, 1, 54, 65, 14]

lista2 = ['G', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

-------------------------------------------------------------------------

# Podemos facilmente checar se determinado valor esta contido na lista
num = 8
if num in lista5:
    print(f"Encontrei o numumero {num}")
else:
    print(f"Não encontrei o numero {num}")
--------------------------------------------------------------------

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)
---------------------------------------------------------------------

# Podemos facilmente contar o numero de ecorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))
--------------------------------------------------------------------

# Adicionar elementos em listas
Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append, nós so conseguimos adicionar um elemento por vez
# lista1.append(1, 5, 4) # ERRO

lista1.append([8, 3, 8, 10])  # Coloca a lista como elemento unico (sublista)
print(lista1)

if [8, 3, 8, 10] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

lista1.extend([123, 44, 67])  # Coloca cada elemento das lista como valor adicional a lista
print(lista1)
---------------------------------------------------------------------------

# Podemos inseriri um novo elemento na lista informando a posição do indice
# OBS: Isso não substitui o valor inicial, o mesmo foi deslocado para a direita da lista.
lista1.insert(2, "Novo Valor")
print(lista1)
-----------------------------------------------------------------------------

# Podemos facilemnete juntar duas listas
# lista1.extend([lista2])
lista6 = lista1 + lista2
print(lista6)
------------------------------------------------------------------------

# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])
--------------------------------------------------------------------

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)
---------------------------------------------------------------

# Contar o tamanho da lista
print(len(lista5))
------------------------------------------------------

# Podemos remover facilmente o ultimo elemento da lista
# OBS: O pop não somente remove o ultimo elemento, mas tambem o retorna
print(lista2)
lista2.pop()
print(lista2)

# Podemos remover um elemento pelo indice
# OBS: Os elemntos a direita deste indice seram deslocados para a esquerda
# OBS: Se não houver elemento no indice no indice informado, teremos o erro de indexerror
lista2.pop(2)
print(lista2)
-----------------------------------------------------------------------------

# Podemos remover todos os elementos ( zerar a lista)
print(lista5)
lista5.clear()
print(lista5)
--------------------------------------------------------------------------------

# Podemos facilmente repetir elemntos em uma lista
nova = [1, 2, 3]
print(nova)
nova *= 3
print(nova)
------------------------------------------------------------------------

# Podemos facilmente converter uma string para uma lista
# Exemplo 1:

curso = 'programção em python'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão o split separa os elemenstos da lista pelo espaço entre elas

# Exemplo 2:

curso = 'programação,em,python'
print(curso)
curso = curso.split(',')
print(curso)
-----------------------------------------------------------------------------

# Convertendo uma lista em uma string

lista6 = ['programação', 'em', 'python']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca esapço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca '@' entre cada elemento e transforma em uma string
curso = ' @ '.join(lista6)
print(curso)
----------------------------------------------------------------------------

# Podemos colocar qualquer tipo de dados em uma lista, inclusive misturando
lista6 = [1, 2, True, 'd']
print(lista6)
--------------------------------------------------------------------------

# Iterando sobre listas

# Exemplo 1 - Utilizando for

soma = 0
for elemento in lista1:
    print(elemento)
    soma += elemento

print(f"A soma dos elementos é {soma}")




#  Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != "sair":
    produto = input(print("Adicione um produto no carrinho ou digite 'sair' para finalizar: ")).lower()
    if produto != "sair":
        carrinho.append(produto)

for produto in carrinho:
    print(produto)




# Ulizando variavies em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)




# Fazemos acesso aos elementos de forma indexeda

#           0          1        2
cores = ['verde', 'amarela', 'azul']
print(cores[0])
print(cores[1])
print(cores[2])

# Fazer acesso aos elementos de forma indexada inversa
# para entender melhor o indice negativo, pense na lista como um circulo onde o final de um elemento esta ligado ao inicio da lista


print(cores[-1])  # azul
print(cores[-2])  # amarelo
print(cores[-3])  # verde




for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1


# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

---------------------------------------------------------------
# Lista aceita valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(42)
lista.extend([42])
print(lista)

-----------------------------------------------

# Metodos não tão importantes mas tambem uteis
# Encontrar o indice de um elemento na lista
numeros = [5, 6, 7, 10, 5]

# Em qual indice esta o valor 6?
print(numeros.index(6))

# Em qual indice esta o valor 6?
print(numeros.index(10))

# OBS: Caso não tenha este elemento na lista será apresentado erro

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # buscando apartir do indice 1

# Podemos fazer busca dentro de umrange, inicio/fim
print(numeros.index(6, 1, 4))  # Buscar o indice do valor 6, entre os indices 1 a 6

----------------------------------------------------------------

# Revisão de slicing
# Lista[inicio : fim : passo]
# Range[inicio : fim : passo]

# Trabalhando com slice em lista com o parametro "inicio"

lista = [1, 2, 3, 4, 5]
print(lista[1:])  # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com o parametro 'fim'
print(lista[:2])  # Começa em 0, pega ate o indice 2

print(lista[1:3])  # Começa em 1 e vai ate o indice 3

# Trabalhando com slice de lista com o parametro 'passo'
print(lista[0::2])  # Começa em 0 e vai ate o final de 2 em 2
-----------------------------------------------------------------------

# invertendo valores em uma lista
nome = ['valdinei', 'mello']
nome[0], nome[1] = nome[1], nome[0]
print(nome)

nome.reverse()
print(nome)
----------------------------------------------------------------------

# Soma*, valor maximo*, vamor minimo*, tamanho*
# * Se os valores todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # soma
print(max(lista))  # valor maximo
print(min(lista))  # valor minimo
print(len(lista))  # tamanho
---------------------------------------------------------------------

# Transforma uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
------------------------------------------------------------------------

# Desempacotamento de lista

lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)
----------------------------------------------------------------------------

# Copiando uma lista para a outra (Shallow Copy e Deep Copy)
# Forma 1
# Veja que ao utilizarmos o lista.copy() copiamos os dados para uma nova lista (Deep Copy)
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(7)
print(nova)

# Forma 2 - Shallow Copy
# Veja que utilizamos a copy via atribuição e copiamos os dados da lista para a nova lista que alterou tambem a lista

lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(8)

print(lista)
print(nova)


"""


lista = [1, 2, 3]
lista.pop(2)

print(lista)
