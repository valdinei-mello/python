"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?

- Quando uma linguagem de programação suporta HOP, indica que podemos ter funções que retornam outras funções como
 resultado, ou mesmo que podemos passar funções como argumentos para outras funções e até mesmo criar variaveis do tipo
 de funções nos programas.

 OBS: Na seção de funções, utilizamos isso.

Em python as funções são cidadões de primeira classe, first class citizen


-----------------------------------------------------

# Exemplos  - Definindo as funções

def somar(n1, n2):
    return n1 + n2


def subtrair(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    return n1 / n2


def calcular(n1, n2, funcao):
    return funcao(n1, n2)


# Testando as funções


print(calcular(4, 3, somar))
print(calcular(4, 3, subtrair))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

-------------------------------------------

# Nested Functions - Funções Aninhadas

# Em python podemos ter funções dentro de funções, que são conhecidas por Nestes Functions ou
# também Inner Functions (Funções Internas)

# Exemplo

from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(("E ai", 'Suma daqui', 'Gosto de você'))
    return humor() + pessoa

# Testando


print(cumprimento(' valdinei'))

print(cumprimento(' dinei'))

----------------------------------------

# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahah', 'kkkkkkk', 'rsrsrsrsrs'))
    return rir()

# Testando


rindo = faz_me_rir()
print(rindo)



"""


# Inner Functions , podem acessar o escopo de funções externas

from random import choice


def faz_me_rir_novamente(pessoa):
    def rir():
        risada = choice(("hahahahah", "kkkkkk", "wowowowowowo"))
        return f'{risada}, {pessoa}'
    return rir


rindo = faz_me_rir_novamente('ney')
print(rindo())
