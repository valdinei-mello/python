"""
Doctestes

Doctestes são testes que colocamos na docstring das funç~pes python.

Para rodar um test do doctest:
    python -m doctest -v nome_do_modulo.py

# Saida do testes:
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    Doctestes
1 items passed all tests:
   1 tests in Doctestes.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.


"""


def soma(a, b):
    """
    Soma os numeros 'a' e 'b'

    >>> soma(1, 2)
    3
    """
    return a + b

# Outro exemplo aplicando o TDD


def duplicar(valores):
    """
    Duplicar os valoree em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]
    """
    return [elemento * 2 for elemento in valores]
