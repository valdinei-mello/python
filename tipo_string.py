"""
Tipo String

O python um dado é considerado do tipo string sempre que:
 - Estiver estre aspas simples;
 - Estiver entre aspas duplas;
 - Estiver entre aspas simplas triplas;
 - Estiver entre aspas duplas triplas.

 nome = 'Geek'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

print(nome.upper()

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:4])  # Slice de string
print(nome[5:15])  # Slice de string

# [   0,        1      ]
# ['Geek', 'University']
print(nome.split()[0])
print(nome.split()[1])
"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,   13,  14]
# ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
nome = "Geek University"

"""
[::-1] = Começa do primeiro elemento va até o ultimo elemento e inverta
"""
print(nome[::-1])  # Inversão da string Pythonico
print(nome.replace('e', 'u'))
