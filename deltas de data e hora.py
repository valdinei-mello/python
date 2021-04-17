"""
trablhando com deltas de data e hora

data_inicial: dd/mm/aaaa
data_final: dd/mm/aaaa

delta = data_final - data_inicial
=====================

import datetime

# data de hoje
data_hoje = datetime.datetime.now()

# data do evento
aniversario = datetime.datetime(2021, 3, 3, 0)

tempo_para_evento = aniversario - data_hoje

print(tempo_para_evento)

===================================


"""

import datetime


data_compra = datetime.datetime.now()
print(data_compra)

data_pagamento = datetime.timedelta(days=3)
print(data_pagamento)

data_boleto = data_compra + data_pagamento
print(data_boleto)


