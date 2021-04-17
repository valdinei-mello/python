"""
Listas Aninhadas

- Algumas linguegens de progrmação possuem uma estrutura de dados, chamadas de arrays:
    - Unidimensionais ( Arrays/Vetores)
    - Multidimensionais (Matrizes)

Em python nós temos as listas

numeros = [1, 'a', 3.4, TRUE, 5, 6]



# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(listas)

# Como fazemos para acessar os dados ?
print(listas[0][2])  # Acesso ao numero 3
print(listas[2][2])  # Acesso ao numero 9


# Iterando com loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)


# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

"""


# outros exemplos
# Gerando um tabuleiro ou matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for numero in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)]for numero in range(1, 4)]
print(velha)

# Gerando valores inicias

print([['*' for i in range(1, 4)]for j in range(1, 4)])



