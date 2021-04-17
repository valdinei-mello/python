"""
Reversed

OBS: Não cinfunda coma função reverse() que estudamos na lista.

A função reverse() só funciona em listas, já a função reversed() funciona co qualquer iteravél.
Sua função é inverter o iteravél.

Ele retorna um iteravél chamado List Rverse Interator.


"""

# Exemplos

lista = [1, 2, 3, 4, 5]
res = reversed(lista)

print(lista)
print(type(res))

# Podemos converter o elemento para Tupla, Lista ou Conjunto
print(tuple(reversed(lista)))
print(list(reversed(lista)))
print(set(reversed(lista)))  # Em Conjuntos não definimos a ordem dos elementos

# Podemos iterar sobre o reversed
for letra in reversed('valdinei de mello'):
    print(letra, end='')
print('')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('valdinei de mello'))))

# Já vimos como fazer isso mais facil com o slice de string
print('valdinei de mello'[::-1])

# Podemos tambme utilizar o revered() para fazer um loop for reverso
for num in reversed(range(10)):
    print(num)

# Apesar que tambem que ja vimos como fazer isso utilizando o proprio range()
for n in range(10, 0, -1):
    print(n)


