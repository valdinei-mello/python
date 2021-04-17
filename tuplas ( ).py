"""
Tuplas (tuple)

Tuplas são bastatantes parecidas com listas.

Existe basicamente 2 diferenças:
1- As tuplas são representadas por ()
2- As tuplas são imutaveis: isso significa que se criar uma tupla ela não muda . Toda operação em uma tupla
gera uma nova tupla.

--------------------------------------------------
# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5)
print(type(tupla1))
print(tupla1)

tupla2 = 1, 2, 3, 4, 5
print(type(tupla2))
print(tupla2)

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (9)  # Isso não é uma tupla!
print(type(tupla3))
print(tupla3)

tupla4 = (4, )  # Isso é uma tupla
print(type(tupla4))
print(tupla4)

tupla5 = 4,
print(type(tupla5))
print(tupla5)

# CONCLUSÃO: Tuplas são definidas pela virgula e não pelo uso do ()
(4) - Não é tupla
(4,) - É tupla
 4, - É tupla
-----------------------------------------------------

# Podemos gerar uma tupla dinamicamente com o range(inicio, fim, passo)
tupla = tuple(range(10, 20, 2))
print(tupla)
----------------------------------------------------------

# Desempacotamento de tupla
# OBS: Gera erro se colocar um numero diferente de elementos para despacotar

tupla = ('Geek University', 'Programação em python')
escola, curso = tupla

print(escola)
print(curso)
--------------------------------------------------
# Metodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis

----------------------------------------------------
# Soma, valor maximo, valor minimo, e tamanho
# se os valores forem todos inteiros ou reias

tupla = (1, 2, 3, 4, 5)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
--------------------------------------------------

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # tuplas são imutaveis
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2 # tuplas são imutaveis, mas podemos sobrescrever seus valores
print(tupla3)
---------------------------------------------------

# Verificar se determinado elemnto está contido na tupla:

tupla = (1, 2, 3, 4)
print(3 in tupla)
-----------------------------------------------

# Iterando sobre uma tupla

tupla = (1, 2, 3, 4)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
------------------------------------------------------

# Contando elementos dentro de uma tupla:

tupla = ('a', 'c', 'a', 'c', 'q')
print(tupla.count("a"))
-------------------------------------------------------------

# Convertende string em tupla

nome = tuple("Valdinei")
print(nome)
print(nome.count('i'))

-----------------------------------------------------------

# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos mudar os dados contidos em uma coleção:

# Exemplo 1:

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O acesso a elementos é semelhante de uma lista
print(meses[1])

# Interar com while

i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice um elemento esta na tupla
# OBS: Caso o elemento não exista, será gerado erro

print(meses.index('Junho'))

# Slicing
# tupla[inicio, fim, passo]

print(meses[0::])
------------------------------------------------------

# Porque utilizar tuplas:
# - Tuplas são mais rapidas do que listas.
# - Tuplas deixa o código mais seguro, isso poruqe trabalhar com elementos imutaveis traz segurança para o código
-------------------------------------------------------

# Copiando uma tupla para outra

tupla = (1, 2, 3,)
print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow Copy
print(nova)

print(tupla)

"""




