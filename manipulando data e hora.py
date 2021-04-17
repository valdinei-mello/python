"""
Manipulando Data e Hora

Python tem um modulo built-in( integrado) para se trabalhar com data/hora chamda datetime

============================

import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# Retorna data e hora atual
print(datetime.datetime.now())  # (2020-10-28 20:00:43.769374)

# Representação (datetime.datetime(year, month, day, hour, minute, second, microsecond))
print(repr(datetime.datetime.now()))

# replace() para fazer ajuste na data/hora
inicio = datetime.datetime.now()

# Alterando o horaio para 5 horas, 0 minutos, 0 segundos, o microsegundos
inicio = inicio.replace(hour=5, minute=0, second=0, microsecond=0)
print(inicio)

==========================================
# Recebndo dados do usuario e convertendo para data

import datetime

evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))
print(type('31/12/2020'))
print(evento)


aniversario = input("Informa a sua data de nascimento (dd/mm/yyy): ")
print(aniversario)

nova_data = aniversario.split('/')
print(nova_data)
print(nova_data[0])
print(nova_data[1])
print(nova_data[2])

data_python = datetime.datetime(year=int(nova_data[2]), month=int(nova_data[1]), day=int(nova_data[0]))
print(data_python)



"""

import datetime

evento = datetime.datetime.now()

# Acesso individual dos elementos data/hora
print(evento.year)  # Ano
print(evento.month)  # Mês
print(evento.day)  # Dia
print(evento.hour)  # Hora
print(evento.minute)  # Minutos
print(evento.second)  # Segundos
print(evento.microsecond)  # Microsegundos


