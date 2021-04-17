"""
Sorted

OBS: Não confunda com a função sort() que já estudamso em lista, o sort() só funciona em listas.

Podemoa utilizar o soreted() com qualquer iteravel.

Como o proprio nome diz, sorted() serve para ordenar.

OBS: O soreted() sempre retorna uma lista com os elementos do iterável ordenados.

numeros = [6, 5, 8, 1]
print(numeros)
print(sorted(numeros))  # Ordenar do maior para o menor
print(numeros)
---------------------------

# Adicionando parametros ao sorted()
print(sorted(numeros, reverse=True))  # Neste caso ele ordena do maior para o menor

------------------------------
# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {'username': "samuel", 'tweets': ['Eu adoro bolo', 'Eu adoro pizaa']},
    {'username': "marcos", 'tweets': ['Eu adoro bacon']},
    {'username': "jubileu", 'tweets': [], 'cor': 'preto'},
    {'username': "roberto", 'tweets': []},
    {'username': "maria", 'tweets': ['Eu adoro alface', 'Eu adoro arroz']},
]

print(usuarios)

# Ordenando pelo username - ordem alfabetica
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

"""

# ultimo exemplo:

musicas = [
    {'titulo': 'acdc', 'tocou': 3},
    {'titulo': 'iron', 'tocou': 10},
    {'titulo': 'ramones', 'tocou': 8},
    {'titulo': 'metalica', 'tocou': 13},
    {'titulo': 'calypso', 'tocou': 1}
]
# ordena da menos tocada a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# ordena da mais tocada a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

# ordena pela qtde de letras do titulo
print(sorted(musicas, key=lambda titulo: len(titulo['titulo'])))









