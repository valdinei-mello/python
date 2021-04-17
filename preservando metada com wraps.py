"""
Preservando Metada com Wraps

Metadados: São dados intrisecos em arquivos.

Wraps: São funções que envolvem elementos com diversas finalidades


==========================

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma função(logar) dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui esta a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    # Soma dois numeros
    return a + b

# Testando


# print(soma(1, 9))
print(soma.__name__)  # soma
print(soma.__doc__)  # soma dois numeros


"""


# Resolvendo Problema

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função(logar) dentro de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui esta a documentação {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b

# Testando


print(soma(1, 9))
print(soma.__name__)  # soma
print(soma.__doc__)  # soma dois numeros
