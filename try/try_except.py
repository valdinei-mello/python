"""
O bloco try / except


Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso codigo. Prevenindo que o programa para de
funcionar e o usuario recebe menssagem de erros.

A forma geral mais simples é :

try:
    //Execeução problematica
except:
    //O que deve ser feito em caso de problemas

===========================
# Exemplo 1: Tratando um erro generico

try:
    geek()
except:
    print("Deu erro")

# Tente executar a função geek(), caso encontre erros, imorima a msg de erro.

======================
# Exemplo 2: Tratando um erro especifico

try:
    geek():
except NameError:
    print("Deu erro")

==============================
# Exemplo 3: Tratando um erro especifico com detalhes do erro

try:
    geek()
except NameError as err:
    print(f"Deu erro: {err}")

===============================
# Podemos efetuar diversoso tratamentos de erros de uma só vez:

try:
    #len(2)
    ney()
except NameError as erra:
    print(f"Deu NameError: {erra}")
except TypeError as errb:
    print(f'Deu TypeErro: {errb}')
except ZeroDivisionError as errc:
    print(f'Deu ZeroDivisionError: {errc}')


"""


def imprimir(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as err:
        return None


dic = {'nome': 'valdinei'}
print(imprimir(dic, 'nome'))





