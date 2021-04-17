"""
modeulo collections - ordered dict


# em um dicoinario a ordem de inserção do elementos não é garantida
dic = {'a': 1, 'b': 2, 'c': 3}

for chave, valor in dic.items():
    print(f'{chave}: {valor}')
--------------------------------------------------

# OrderedDict = é um dicionario, que nos garante a ordem de inserção dos elementos

# fazendo o import
from collections import OrderedDict

dic = OrderedDict({'a': 1, 'b': 2, 'c': 3})

for chave, valor in dic.items():
    print(f'{chave}: {valor}')

"""
from collections import OrderedDict

# entendendo a dferença entre dict e ordered dict
# dicionarios comuns
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # true / false ?? true= ja que a ordem dos elementos não importa para o dicionario

# ordered dict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # true / false ?? false = ja que a ordem dos elementos importa




