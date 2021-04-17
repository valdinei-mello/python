"""
Ranges

- Precisamos conhecer o loop for para usar os ranges;
- Precisamos conhecer o rqnge para tranlhar melhor com loops for.

Ranges são ytilizados para gerar seguencias numericas, não de forma aleatoria
mas sim de maneiras especificas


Formas Gerais:

#Forma 1:
range(valor_de_parada)

OBS: Valor de parada não inclusive (inicio padrão 0, e passo 1 em 1 )
# Exemplo Forma 1
for numero in range(11):
    print(numero)
-------------------------------------------------------
#Forma 2:
range(valor inicio, valor parada)

OBS: Valor de parada não inclusive (iniio especificado pelo usario e passo 1 em 1 )
# Exemplo Forma 2
for numero in range(1, 11):
    print(numero)
-----------------------------------------------------------
# Forma 3:
range(valor de inicio, valor de parada, passo)

OBS: Valor de parada não inclusive (iniio especificado pelo usario e passo especificado pelo usuario)
# Exemplo Forma 3
for numero in range(1, 10, 2):
    print(numero)
---------------------------------------------------------
# Forma 4 (Inversa):
range(valor de inicio, valor de parada, passo)

OBS:  Valor de parada não inclusive (valor inicio especificado pelo usario e passo especificado pelo usuario)
# Exemplo Forma 4
for numero in range(10, -1, -1):
    print(numero)
-----------------------------------------------------------------
"""

# Exemplo Forma 4
for numero in range(10, -1, -1):
    print(numero)
