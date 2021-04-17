"""
ANY e ALL

All() = Retorna True, se todos o elemntos do iteravel são veradeiros ou ainda se o iteravel esta vazio.

# Exemplo All():

print(all([1, 2, 3, 4]))  # todos os numeros são verdadeiros ? True
print(all([0, 1, 2, 3, 4]))  # todos os numeros são verdadeiros ? False
print(all([]))  # todos os numeros são verdadeiros ? True

nomes = ['maria', "marcos", "marcela", "mario"]

print(all([nome[0] == 'm' for nome in nomes]))

print(all(numero for numero in [4, 10, 8, 4] if numero % 2 == 0))


Any() = Retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio, retorna False

"""

print(any([1, 2, 3, 4]))  # True
print(any(['', (), 0, False]))  # False








