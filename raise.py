"""

Levantando os proprios erros com raise


raise  = Lança exceções

OBS: O raise não é uma função, é uma palavra reservada, assim como def ou quqluer outra palavra em python.

Para simplificar, pesne no raise como sendo util para crir nossas proprias execeções e mensagens de erro.

A forma geral de utilização é :

raise TipoError('Menssagem de erro')


# Exemplo:

def color(texto, cor):
    if type(texto) is not str:
        raise TypeError("O texto precisa ser uma string ")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser uma string ")

    print(f"O {texto} é da cor {cor} ")


color('sol', 14)

====================================

def color(texto, cor):
    cores = ('verde', 'amarelo', 'azul')
    if type(texto) is not str or type(cor) is not str:
        raise TypeError("O texto precisa ser uma string ")
    if cor not in cores:
        raise ValueError('O texto digitado não esta contido no padrão ')

    print(f"O {texto} é da cor {cor} ")


color('sol', 'amarelo')

"""


def color(texto, cor):
    cores = ('verde', 'amarelo', 'azul')
    if type(texto) is not str or type(cor) is not str:
        raise TypeError("O texto precisa ser uma string ")
    if cor not in cores:
        raise ValueError('O texto digitado não esta contido no padrão ')

    print(f"O {texto} é da cor {cor} ")


color('sol', 'amarelo')



