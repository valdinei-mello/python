"""
Decoradores com Difrentes Assinaturas


# Relembrando


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome)
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o {nome.upper()}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor !'


# Testando 1:

print(saudacao('Valdinei de mello'))
print('')
print(ordenar('picanha', 'batata frita'))


# Para resolver utilizamos um padrão de projeto chamado 'Decorators Pattern'

# A assinatura de uma função é representada pelo seu retorno , nome e parametro de entrada.

=======================================

# Refatorando com decorators pattern


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor !'


# Testando 1:

print(saudacao('Valdinei de mello'))
print('')
print(ordenar('picanha', 'batata frita'))


@gritar
def lol():
    return 'lol'


print(lol())

# OBS: Vale lembrar que podemos usar parametros nomeados

print(ordenar(principal='arroz e feijão', acompanhamento="carne"))


"""

# Decorator com argimentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return args


@verifica_primeiro_argumento(10)
def soma_dez(n1, n2):
    return n1 + n2


# Testes

print(soma_dez(10, 12))
# print(soma_dez(1, 258)) # Primeiro valor precisa ser 10


print(comida_favorita('pizza', 'carne'))
# print(comida_favorita('bolo', 'pizza')) # Primeiro valor precisa ser 'pizza'



