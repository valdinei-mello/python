"""
Assertions (Afirmações / Checagens / Questionamentos)


Em python utilizamos a palvra resevada 'assert' para realizar simples afirmações
utilizadas nos testes.

Utilizamos o 'assert' em uma expressão que queremos chegar se é valida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError.

# OBS: Nós podemos especidifcar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada.

#OBS: A palavra 'assert' pode ser utilizada em qualquer função ou codigo nosso... não precisa ser exclusiva nos testes.

# ALERTA: Cuidado ao utilizar 'assert'

Se um program python for executado com o parametro -O, nenhum asseetion será validada,
ou seja, todas as suas validações ja eram.

===============================

def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos precisam ser positivo'
    return a+b


print(soma_numeros_positivos(5, 2))  # 7
print(soma_numeros_positivos(5, -2))  # AssertionError

==============================




"""


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'pastel',
        'lanche',
        'sorvete'
    ], 'A comida precisa ser fast food'
    return f'Estou comendo {comida}'


print(comer_fast_food('arroz'))  # AssertionError
print(comer_fast_food('pastel'))  # Comendo pastel


# ALERTA: Cuidado ao utilizar 'assert'
