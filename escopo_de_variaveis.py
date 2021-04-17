"""
Escopo de Variaveis

Dois casos de escopo:

1 - Variavies globais;
    - Variaveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa.

2 -  Variavies locais;
    - Variaveis locais são reconhecidas apenas no bloco onde foram declaradas, ou sej,
    seu escopo esta limitado ao bloco onde foi declarada

Para declarar variaveis em Python fazemos:

nome_da_variavel = valor|_da_variavel

Python é uma linguagem de tipagem dinamica . Isso significa que
ao declarar uma variavel, nós não colocamos o tipo de dado a ela.
Este tipo é inferido ao atribuirmos o valor a mesma.

Exemplo em C:
int numero = 42

Exemploem Java:
int numero = 42
"""

numero = 42  # Variavel global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10  # a variavel novo esta declarada localmente, dentro do bloco do if
    print(novo)



