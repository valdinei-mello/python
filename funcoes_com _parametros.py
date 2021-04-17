"""
Funções com parametro ( de entrada)

- funções que recebem dados para serem processados dentro da mesma;

Se pensarmos em um programa qualquer, geralmente temos:
    - entrada, processamento, saida

se pensarmos em uma função, já sabemos que temos funções que:
    - não possuem entrada;
    - não possuem saída;
    - possuem entrada mas não possuem saida;
    - não possuem entrada mas possuem saida;
    - possuem entrada e saida;

-------------------------------------------
# Refatorando uma função

def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(5))
print(quadrado(10))
-----------------------------------------

# refatorando a função

nome = input("Digite o nome do aniversariante: ")

def cantar_parabens(aniversariante):
    print('parabens')
    print('muitas felicidades')
    print('saude')
    print(aniversariante)

cantar_parabens(nome)
------------------------------------------

# funções podem ter N parametros de entrada, ou seja, podemos receber como entrada em uma funçãoquantos parametros necessarios.
Eles são separados por virgula;

# Exemplos


def soma(a, b):
    return a+b


def multiplicação(a, b):
    return a*b


def outra(a, b, msg):
    return (a + b) * msg


print(soma(4, 2))
print(multiplicação(4, 2))
print(outra(7, 2, ' blz'))


# OBS: se informarmos parametros a mais / menos que o esperado pela função , vai dar erro
---------------------------------------

# nomeando parametros

def nome_completo(nome, sobrenome):
    return f"Seu nome completo é {nome} de {sobrenome}"


print(nome_completo("Valdinei", "Mello"))


# Diferença entre parametro e argumento:
    # Parametros: são variaveis declaradas na definição de uma função;
    # Argunmentos: são dados passados durante a execução de uma funçõa;

# A ordem dos parametos importa!

nome = 'didi'
sobrenome = 'moco'

# Argumentos nomeados (Keyword Arguments)
    # Caso utilizemos nomes nos parametros nos argumentos para informa-los, podemos utilizar qualquer ordem;

print(nome_completo(nome='marcos', sobrenome='pontes'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome=sobrenome, nome=nome))

----------------------------------------------------



"""


# Erro comun na utilização do return

def numero_impar(numero):
    total = 0
    for num in numero:
        if num % 2 != 0:
            total += num

    return total


lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(numero_impar(lista))



