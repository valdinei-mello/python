"""
Funções com parametros padrão ( Default Parameters

- Funções onde a passagem de parametro seja opcional;

# Exemplo de função onde passagem de parametro seja opcional
print('Valdinei de Mello')
print()
--------------------------------

# Exemplo de função onde a passagem de parametros seja obrigatoria;

def quadrado(numero):
    return numero ** 2


print(quadrado(3))
print(quadrado()) # Type Error
-----------------------------------------

def exponencial(numero, potencial=2):
    return numero ** potencial


print(exponencial(2, 3))  # 2*2*2=8

print(exponencial(4))  # por padrão eleva ao quadrado
print(exponencial(4, 3))  # eleva a potencia informado pelo usuario

# OBS:
# se o usuario passar somente um parametro, este será atrinuido ao parametro numero, e será calculado o quadrado;
# se o usuario passar 2 elementos, o primeiro será atrinuido ao parametro numero e o segundo ao parametro potencia.

-------------------------------

# OBS: em funções python, os parametros com valores DEFAULT, devem sempre estar ao final da declaração;

# ERRO!
def teste(num=2, potencia):
    return  num ** potencia

# CORRETO
def teste(potencia, num=2):
    return  num ** potencia
----------------------------------------

# outros exemplos:

def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))
print(soma(4))  # TypeError
print(soma())  # TypeError
----------------------------------------

# Exemplo mais complexo


def mostra_informação(nome='valdinei', instrutor = False):
    if nome == 'valdinei' and instrutor:
        return f"Bem vindo {nome} !"
    elif nome == 'valdinei':
        return f"Eu pensei que você fosse o instrutor {nome}"
    return f"Olá {nome} !!"


print(mostra_informação())
print(mostra_informação(instrutor=True))
print(mostra_informação('Ozzy'))
print(mostra_informação(nome='Naty'))
---------------------------------------------------

# Porque utilizar parametro com valor padrão ?
    # Nos permite ser mais flexivel;
    # Evita erros comparametros incorretos;
    # Nos permite trabalhar com exemplos mais legiveis de codigo;

# Quais tipos de dados podemos utilizar como valores default como parametros?
    # Qualquer tipo de dados:
        # numeros, strings, float, booleanos, listas, ...;

---------------------------------------------------------------

# Exemplos de funções com funções padrão

def soma(n1, n2):
    return n1 + n2


def mat(n1, n2, fun=soma):
    return fun(n1, n2)


def sub(n1, n2):
    return n1 - n2


print(mat(2, 3))
print(mat(2, 2, sub))
------------------------------

# Escopo - Evitar problemas e confusões...

# Variaveis globais
# Variaveis locais


instrutor = "geek"


def diz_oi():
    instrutor = 'python'  # Variavél local
    return instrutor


print(diz_oi())




def diz_oi():
    prof = 'ney'
    return prof


print(diz_oi())
print(prof) # NameError

-----------------------------------------

# ATENÇÃO com variavies globais

total = 0


def incrtement():
    total += 1  # UnboundLocalError (A variavel local esta sendo usada sem ter sido inicializada)
    return total


print(incrtement())
----------------------------

# ATENÇÃO com variavies globais

total = 0


def incrtement():
    global total  # Avisando que queremos utilizar a variavel global
    total += 1
    return total


print(incrtement())

---------------------------------

# Podemos ter funções que são declaradas dentro de funções, e tbm tem um forma especial de escopo de variavel

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador += 1
        return contador
    return dentro()


print(fora())

"""






