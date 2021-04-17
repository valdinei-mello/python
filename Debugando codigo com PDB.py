"""

Debugando com PDB : Python Debugger

Bug = Inseto

=======================


# OBS: A utilização do print() para debugar codigo é uma pratica ruim.

def dividir(a, b):
    print(a + '-' + b)
    try:
        return int(a) + int(b)
    except:
        return "Deu erro "


print(dividir(4, 7))

===============

# Existem formas mais proficionais de se fazer esse debug, utilizando o debugger
# Em python podemos fazer isso em diferentes IDEs, como o PyCharm ou utilzando o PDB do python

# Exemplo com o PyCharm

def dividir(a, b):
    try:
        return int(a) + int(b)
    except:
        return "Deu erro "

print(dividir(4, 7))

=========================
# Exemplo 1 com PDB - Python Debugger

# Para utilizar o python debugger, precisamos *importar a biblioteza pdb e então utilizar a função set_trace()

# Comandas básios do pdb
# l (listar onde estamos no código)
# n (proxima linha)
# p (imprimi variável)
# c (continua a execução - finaliza o debugger)

import pdb

nome = 'valdinei'
sobrenome = 'mello'
pdb.set_trace()
nomecompleto = nome + ' ' + sobrenome
curso = 'python'
final = nomecompleto + ' faz o curso de ' + curso

print(final)

========================

# Exemplo 2 com PDB - Python Debugger

# Para utilizar o python debugger, precisamos *importar a biblioteza pdb e então utilizar a função set_trace()

# Comandas básios do pdb
# l (listar onde estamos no código)
# n (proxima linha)
# p (imprimi variável)
# c (continua a execução - finaliza o debugger)

nome = 'valdinei'
sobrenome = 'mello'
import pdb; pdb.set_trace()
nomecompleto = nome + ' ' + sobrenome
curso = 'python'
final = nomecompleto + ' faz o curso de ' + curso

print(final)

# Porque utilizar este formato ?
# O debug é utilizado durante o desenvolvimento.
# Custumamos realizar todos os importes de bibliotecas no incio do arquivo. Por isso ao invês de colocarmso o
# import do pdb no inicio do arquivo nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção

================================

# Exemplo 3 com PDB - Python Debugger

# Para utilizar o python debugger, precisamos *importar a biblioteza pdb e então utilizar a função set_trace()

# * no python apartir 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado com função built-in (integrada) chamada breakpoint()

# Comandas básios do pdb
# l (listar onde estamos no código)
# n (proxima linha)
# p (imprimi variável)
# c (continua a execução - finaliza o debugger)

nome = 'valdinei'
sobrenome = 'mello'
breakpoint()
nomecompleto = nome + ' ' + sobrenome
curso = 'python'
final = nomecompleto + ' faz o curso de ' + curso

print(final)

"""

# OBS: cuidado com os nomes das variaveis e os comandos do pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 2, 3, 4))

# Como os nomes das variavies são os mesmos do comando pdb, devemos utilizar o comando 'p' para imprimir as variavies.
# ou seja, p nomedavariavel


















