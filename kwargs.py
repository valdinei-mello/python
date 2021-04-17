"""
**kwargs

Poderiamos chamr este parametro de **xix, mas por convenção chamamos de **kwargs;

Este é so mais um parametro, mas diferente do *args que coloca os valores em uma tupla, o **kwargs exige que
utilizemos parametros noeados, e transforma esses parametros em um dicionario.



# Exemplo:


def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor de {pessoa.title()} é {cor}')


cores(ney='azul', marcos='amarelo')

# OBS:Os parametros *args e **wkargs não são obrigatorios

cores()
cores(lima='verde')
-------------------------------------------------

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return 'Você recebeu um cumprimento pythonico'
    elif 'geek' in kwargs:
        return 'Voce esta prestes a receber um cumprimento pythonico'
    return 'Não tenho certeza de quem é voce'


print(cumprimento_especial())
print(cumprimento_especial(geek='python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))
-------------------------------------

# Nas nossas funções podemos ter NESTA ORDEM:
    # - Parametros obrigatorios:
    # - *args
    # - Parametros default (parametros não obrigatorios):
    # - **kwargs

def minha_função(num, *args, solteiro=False, **kwargs):
    print(num)
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)


minha_função(5, [1, 2, 3, 4, 5], solteiro=True, nome='julia')
-----------------------------------------

# Entendo por que é importante manter a ordem dos parametrso na declaração

# Função com a ordem correta de parametrsos


def mostrar_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostrar_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))
----------------------------------------------

# Desempacotar com kwargs:

def mostrar_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'valdnei', 'sobrenome': 'mello'}

print(mostrar_nomes(**nomes))

"""


def soma_multiplos_numeros(a, b, c):
    print(a+b+c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conj = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conj)


dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)


# OBS: Os nomes da chave em um dicionario devem ser os mesmo dos parametros da função;




