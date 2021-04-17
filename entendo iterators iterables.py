"""
Entendo Iterators e Iterables

Iterators:
    - Um objeto que pode ser iterado
    - UM objeto que retorna um dado, sendo um elemnto por vez quando uma função next () é chamada;

Iterables:
    - Um objeto irá retornar um iterator quando a função iter() for chamada.

========================================

nome = 'dinei'  # é um iterable mas não é um iterator
numeros = [1, 2, 3, 4]  # é um iterable mas não é um iterator


it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))


print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))



"""

nome = 'dinei'

for letra in nome:
    print(letra)


