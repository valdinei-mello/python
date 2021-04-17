"""
Metodos de data e hora


import datetime

#  Com o now() podemos especificar um timezone (fuso horario)
agora = datetime.datetime.now()  # now == agora
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()  # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))

===============================

import datetime

# Mudanças ocorrendo a meia-noite  - combine()

manutancao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutancao)
print(type(manutancao))
print(repr(manutancao))

========================================

import datetime

# Encontrar o dia da semana - weekday()
# Os dias da semana do método weekday() começam em Zero, sendo esta a segunda-feira.


manutancao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutancao.weekday())

============================================

import datetime

aniversario = input("Qual sua data de nascimento(dd/mm/aaaa):  ")
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print(f'Você faz aniversário em uma segunda-feira')
elif aniversario.weekday() == 1:
    print(f'Você faz aniversáro em uma terça-feira')
elif aniversario.weekday() == 2:
    print(f'Você faz aniversário em uma quarta-feira')
elif aniversario.weekday() == 3:
    print(f'Você faz aniversário em uma quinta-feira')
elif aniversario.weekday() == 4:
    print(f'Você faz aniversário em uma sexta-feira')
elif aniversario.weekday() == 5:
    print(f'Você faz aniversário no sábado')
else:
    print(f'Voce faz aniversário no domingo')


===================================

import datetime

#  Formatando datas/horas com strtime() (String Format Time)
# dd/mm/aaaa

hoje = datetime.datetime.today()
print(hoje)

hoje_formatado = hoje.strftime('%d/%m/%y')
print(hoje_formatado)

======================================

import datetime

def formata_data(data):
    if data.month == 1:
        return f'{data.month} de Janeiro de {data.year}'

    elif data.month == 2:
        return f'{data.month} de Fevereiro de {data.year}'

    elif data.month == 3:
        return f'{data.month} de Março de {data.year}'

    elif data.month == 4:
        return f'{data.month} de Abril de {data.year}'

    elif data.month == 5:
        return f'{data.month} de Maio de {data.year}'

    elif data.month == 6:
        return f'{data.month} de Junho de {data.year}'

    elif data.month == 7:
        return f'{data.month} de Julho de {data.year}'

    elif data.month == 8:
        return f'{data.month} de Agosto de {data.year}'

    elif data.month == 9:
        return f'{data.month} de Setembro de {data.year}'

    elif data.month == 10:
        return f'{data.month} de Outbro de {data.year}'

    elif data.month == 11:
        return f'{data.month} de Novembro de {data.year}'

    elif data.month == 12:
        return f'{data.month} de Dezembro de {data.year}'

#  Formatando datas/horas com strtime() (String Format Time)
# dd/mm/aaaa

hoje = datetime.datetime.today()
print(hoje)
print(formata_data(hoje))

=========================================

import datetime

from textblob import TextBlob


def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()
print(formata_data(hoje))

=================================================

import datetime

nascimento = datetime.datetime.strptime('10/4/1998', '%d/%m/%Y')
print(nascimento)

nascimento = input("Qual sua data de nascimento? (dd/mm/yyyy)")
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)


=========================================================

import datetime

# Somente hora

almoco = datetime.time(12, 30, 0)
print(almoco)


==========================



"""


import timeit

# Marcando tempo de execução do nosso codigo com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(10))', number=10000)
print(tempo)



