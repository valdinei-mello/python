"""
FILTER

filter() -  serve para filtara dados de uma determinada coleção.
-------------------------------------------------

# biblioteca para trabalhar com dados estatisticos
import statistics

# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculando a media dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

# OBS: Assim como a função map(), a filter() recebe dois parametros, sendo uma função e um iterável.

res = filter(lambda x: x < media, dados)
print(type(res))
print(list(res))

# OBS: Assim com na função map(), após ser utilizar os dados de filter(), os dados se apagam da memória.
-----------------------------------------------------------

paises = ['', '', 'brasil', 'eua', '', 'peru', 'equador']
print(paises)
resp = filter(None, paises)
print(list(resp))
# ou
print(list(filter(lambda p: len(p) != 0, paises)))

# A diferença entre MAP e FILTER é:
# map() = recebe dois parametros, uma função e um iteravel e retorna um  objeto mapeando a função para cada elemento do iteravel
# filter() = recebe dois elemenros, uma função e um iteravel e retorna um objeto filtrando apenas os elemntos de acordo coma função

--------------------------------------------------

# Exemplo mais complexo

usuarios = [
    {'username': "samuel", 'tweets': ['Eu adoro bolo', 'Eu adoro pizaa']},
    {'username': "marcos", 'tweets': ['Eu adoro bacon']},
    {'username': "jubileu", 'tweets': []},
    {'username': "roberto", 'tweets': []},
    {'username': "maria", 'tweets': ['Eu adoro alface', 'Eu adoro arroz']},
]

# filtar os usuario que estão inativos no Twitter
print(usuarios)

inativos = filter(lambda u: len(u['tweets']) == 0, usuarios)
print(list(inativos))
"""


# Como cominar filter() e map()

nomes = ['vanessa', 'ana', 'maria']

# devemos criar uma lsta contendo "Sua instrutura é " + nome, desde que cada nome tenha menos de 5 carcteres

instrutora = list(map(lambda nome: f'Sua instrutora é: {nome}', filter(lambda n: len(n) <= 5, nomes)))

print(instrutora)

