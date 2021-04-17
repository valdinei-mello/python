"""
Mapas = conhecidos em python como dicionarios

Dicionarios em python sçao representados por chaves {}

------------------------
# Interar sobre dicionario
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave}: {receita[chave]}')
---------------------------------

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])
-------------------------------------------

# Acesando os valores
print(receita.values())

for valor in receita.values():
    print(valor)
---------------------------

# Desempacotamento de  dicionarios
for chave, valor in receita.items():
    print(f'{chave}: {valor}')

"""

receita = {'jan': 100, 'fev': 200, 'mar': 300}


# Soma*, max*, min*, tamanho
# *Se todos os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.items()))



