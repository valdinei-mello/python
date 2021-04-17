"""
Trabalhando com modulos integrados ( Modulos que ja veem instalados no python)
https://docs.python.org/3/library/random.html#module-random
________________________
/Python/Modulos builtin/
------------------------

# Utilizando alias (apelidos) para modulos /funções
import random as rdm

print(rdm.random())

==============================
# Podemos importar todas as funções de um modulo utilizando o *

from random import *

print(random())

=============================

# Utilizando alias (apelidos) para modulos /funções
from random import randint as rdi

print(rdi(5, 89))


"""


# Costumamos a usar tuple para colocar multiplos imports de um mesmo modulo

from random import (
    random,
    randint,
    shuffle,
    choice
)

nome = ['valdinei', 'mello', 'mococa']
print(random())
print(randint(0, 99))
shuffle(nome)
print(nome)
print((choice('mello')))
