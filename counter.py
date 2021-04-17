"""
modulo collections - counter (contar)

collections = high performance container datatypes

counter = recebe um interavel como parametro e cria um objeto do tipo collections counter que é parecido com um
dicionarios, contendo como chave o elemento da lista passada como parametro e
como valor a qtde de ocorrencias deste elemento;


"""

# utilizando o counter
from collections import Counter

# exemplo 1:

lista = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

res = Counter(lista)
print(res)
# veja que para cada o correncia, o counter colocou como chave cada elemnto da lista e como valor a qtde de repetições
# Counter({1: 3, 2: 2, 3: 2, 4: 2, 5: 2, 6: 1})


# exemplo 2:

print(Counter("valdinei de mello"))
# Counter({'i': 2, 'v': 1, 'a': 1, 'l': 1, 'd': 1, 'n': 1, 'e': 1})

# exemplo 3:

texto = """ Python é uma linguagem de propósito geral de alto nível, multiparadigma, suporta o paradigma 
orientado a objetos, imperativo, funcional e procedural. Possui tipagem dinâmica e uma de suas principais 
características é permitir a fácil leitura do código e exigir poucas linhas de código se comparado ao mesmo 
programa em outras linguagens. Devido às suas características, ela é principalmente utilizada para processamento 
de textos, dados científicos e criação de CGIs para páginas dinâmicas para a web. """

palavras = texto.split()
print(palavras)
print(Counter(palavras))
print(Counter(palavras).most_common(5))  # encontrando as 5 palavras com mais ocorrencias no texto

