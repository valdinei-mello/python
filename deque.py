"""
modulo collections - deque

podemos dizer que o deque é uma lista de alta performance.

"""


# importa
from collections import deque

# criando deques
deq = deque('valdinei')
print(deq)

# adicionando elementos no deque
deq.append('m')  # adiciona no final da lista
print(deq)

deq.appendleft('e')  # adiciona no começo da lista
print(deq)

# remover elementos
print(deq.pop())  # remove e retorna o item do final
print(deq.popleft())  # remove e retorna o primeiro item

