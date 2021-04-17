"""
ZIP

zip() = cria um iteravel (zip object) que agrega elementos de cada um dos iteraveis passados como entrada em pares.
--------------------------

# Exemplos

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

zip1 = zip(lista_1, lista_2, 'abc')
print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, set, dicionario

print(list(zip1))

zip1 = zip(lista_1, lista_2, 'abc')
print(tuple(zip1))

zip1 = zip(lista_1, lista_2, 'abc')
print(set(zip1))

zip1 = zip(lista_1, lista_2)
print(dict(zip1))


# OBS: o zip utiliza como parametro o menor tamanho em  iteravel, isso significa se estiver trabalhando com interavel
de tamanhos diferentes, irá para quando os elemsntos do menor iteravel acabar

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista_1, lista_2, lista3)
print(list(zip1))
-----------------------------------

# Podemos utilzar diferentes iteravéis com o zip

lista = [1, 2, 3, 4]
tupla = 1, 2, 3, 4
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

zt = zip(lista, tupla, dicionario.values())
print(list(zt))


# Listas de tuplas

dados = [(1, 2, 3), (4, 5, 6)]
print(list(zip(*dados)))
---------------------

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'ana', 'caio']


final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(dict(final))



"""


