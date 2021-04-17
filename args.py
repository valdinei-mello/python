"""
Entendo o *args

- O *args é um parametro com outro qualquer, isso significa que voce podera chamar de qualquer coisa,
desde que comece com asterisco '*'

Exemplo:

*xis

Mas por convencção, utilizamos o nome *args para defini-lo

Mas o que é o *args?

- O parametros *args utilizado em um função, coloca os valores extras informados como entreda em uma tupla.
Então desde de já lembre-se que tuplas são imutaveis;
------------------------------------

# Exemplos:


def soma_todos_num(n1, n2, n3):
    return n1 + n2 + n3


print(soma_todos_num(4, 2, 3))
----------------------------------

# Entendo o *args


def soma_todos_num(nome, *args):
    return sum(args)

print(soma_todos_num('valdinei'))
print(soma_todos_num('valdinei', 1))
print(soma_todos_num('valdinei', 1, 2))
print(soma_todos_num('valdinei', 1, 2, 3))
print(soma_todos_num('valdinei', 1, 2, 3, 4))
-----------------------------------

# Outro exemplo de utilização de *args


def verificar_info(*args):
    if 'valdinei' in args and 'mello' in args:
        return 'Bem Vindo! '
    return 'Não te conheço ...'


print(verificar_info('valdinei', 'mello'))
print(verificar_info('Ney', 'Mello'))


"""


def soma_todos_num(*args):

    return sum(args)


print(soma_todos_num())
print(soma_todos_num(1, 2, 3, 4, 5))

numeros = [1, 2, 3, 4, 5, 6, 4]

# Desempacotador
print(soma_todos_num(*numeros))


"""OBS: o asterisco serve para que informemos ao python que estamos informando como argumento uma coleção
de dados. Desta forma, ele precisará antes desempacotar este dados"""


