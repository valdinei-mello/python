"""
Instalando e utilizando modulos externos

Utilizamos o gerenciado de pacotes pythom chamada pip - python installer package
Você pode conhcer todos os pacotes externos oficiais em : https://pypi.org/


Colorama = ele é utilizado para permitir impressão de textos coloridos no terminal

from colorama import init
init()

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')

print(Fore.BLACK + Back.LIGHTBLACK_EX + Style.BRIGHT + 'valdinei')




"""


import pydf

pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

