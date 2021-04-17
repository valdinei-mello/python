"""
Modos de arquivos

r = abre para leitura - padrão
w = abre para escrita - sobrescreve caso o arquivo ja exista
x = abre para escrita, somente se o arquivo não existir. Caso o arquivo existir da erro.
a = abre para escrita adcionando o conteúdo no final do arquivo.
+ = aberto para atualização (leitura e escrita)

http://docs.python.org/3/library/functions.html#open


# Exemplo 'x':

try:
    with open('jogos.txt', 'x', encoding='utf-8') as arq:
        arq.write('Teste de conteúdo')

except FileExistsError as err:
    print(f'Arquivo já exite...{err}')

========================

with open('frutas.txt', 'a', encoding='utf-8') as arq:
    while True:
        fruta = input('Digite uma fruta ou sair para finalizar: ')
        if fruta != 'sair':
            arq.write(fruta + '\n')
        else:
            break

=======================

"""

with open('legumes.txt', '+', encoding='utf-8') as arq:
    while True:
        fruta = input('Digite uma fruta ou sair para finalizar: ')
        if fruta != 'sair':
            arq.write(fruta + '\n')
        else:
            break


