"""
Loop For

Loop = Estrutura de repetição
For = Uma dessas estruturas

C ou JAVA

for(int i=0; i< limitador; i++){
//execução do loop
}

PYTHON

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre seguencias ou sobre valores interaveis

Exemplos de iteraveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1,2,3,4]
- Range
    numeros = range{1,10}
----------------------------------------------------------------
# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)
--------------------------------------------------------------
# Exemplo de for 2(Iterando sobre uma lista)
for numero in lista:
    print(numero)
----------------------------------------------------------------
# Exemplo de for 3 (Iterando sobre um range)
range(valor inicial, valor final)
OBS: O valor final não é inclusive

for numero in range(1, 10):
    print(numero)

----------------------------------------------------
Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), ....)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
OBS: Quando não precisamos de um valor usamos inderline para descartar

for valor in enumerate(nome):
    print(valor)

--------------------------------------------------------------
qtde = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0

for n in range(1, qtde+1):
    num = int(input(f"Digite o valor {n} de {qtde} "))
    soma += num
print(f"Sua soma foi {soma}")

----------------------------------------------------------------
nome = "Geek University"
for letra in nome:
    print(letra, end='')
-----------------------------------------------------------------------

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode



---------------------------------------------


# Original: U + 1F618
# Modificado: U0001F618

# Original: U + 1F62D
# Modificado: U0001F62D
from builtins import range

for _ in range(1, 4):
    for i in range(1, 10):
        if i % 2 == 0:
            print(f"\U0001F618" * i)
        else:
            print(f"\U0001F62D" * i)


"""

'inicio, fim, passo'


def contador(n):
    for i in n:
        print(i)


contador('valdinei')

