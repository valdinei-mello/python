"""
try / except / else / finally

Dica de quando e onde tratr codigo:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuario é DESTRUIR seu sistema.



# Else:  é executado xomente se não ocorrer o erro

try:
    num = int(input('Informe um numero: '))
except ValueError as err:
    print(f"Deu erro: {err}")
else:
    print(f"Voce digitou {num}")

============================
# Finally

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print("Voce digitou algo errado !")
else:
    print(f"Você digitou {num}")
finally:
    print("Executando finally")

# OBS: O bloco finally é sempre executado , independente se houve ou não erro na execução.

# O finally geralmente é utilizado para fechar ou desalocar recursos.

========================

# Exemplos mais complexos ERRADO


def dividir(a, b):
    return a / b


try:

    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite outro numero: "))

    print(dividir(n1, n2))

except ValueError as erra:
    print("O valor precisa ser numerico !")

"""

# Exemplos mais complexos CORRETO
# OBS: Você é reposavél pela entradas da sua função, então trate as


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError as err1:
        return 'Valor incorreto'
    except TypeError as err2:
        return "Tipo de dado incorreto"
    except ZeroDivisionError as err3:
        return "Não pode ser divido por ZERO"


n1 = input('Digite um numero: ')
n2 = input("Digite outro numero: ")

print(dividir(n1, n2))




