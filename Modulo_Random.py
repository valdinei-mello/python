"""
Random é o que são modulos ?

- Em python modulos nada mais são que outros arquivos python.

MOdulo random = possui varias funções para gerações de numeros pseudo-aletorios.

==================================================

# OBS: Existem duas formas de utilizar um modulo ou função deste

# Forma 1: Importando todo o modulo ( Não recomendado).

# random() = Gera um número aleátorio entre 0 e 1.

# Ao relaizar o import de todo o modulo , todas as funçãos, atributos, classes, propriedades que estiverem dentro
#  do modulo ficaram em memoria. Caso saiba quais funções precisa utilizar deste modulo, está não seria a forma ideal
#  de utilização. Nós veremos uma forma melhor na forma 2.

import random

print(random.random())

# Veja que para utilizar a fun~ção random () do pacote random, nós utilizamos o nome do apcote e o nome da função
# separados por ponto.

# OBS: não confunda a função random() com o pacote random. Po de parecer confuso , mas a função random()
# é apenas uma função dentro do modulo random.

====================================


# Forma 2: Importando uma função expecifica do modulo.

from random import random

# No importe acima estamos falando: Do modulo random,importe a função random.

for i in range(10):
    print(random())

================================================

# uniform() = Gerar um numero pseudo-aleatório entre os valores estabelecidos.

from random import uniform

for i in range(10):
    print(uniform(3, 7))  # 7 não é incluido

======================================================

# randint() = Gera valores inteiros aleatorios entre os valores estabelecidados.

# Gerador de apostas para a mega sena

from random import randint

for i in range(6):
    print(randint(1, 61), end=',')

==============================================

# choice() = Mostra uma valor aleatório entre um iterável.

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

================================
# shuffle() = Tem a função de embaralhar dados.

from random import shuffle

cartas = ['K', 'J', 'Q', 'A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(cartas)
shuffle(cartas)
print(cartas)

"""




