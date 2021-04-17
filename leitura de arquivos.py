"""
Leitura de Arquivos

Para ler o conteudo de um arquivo em python, utilizamos a função integrada open(),
que literalmente significa 'abrir'

open() = Na forma mais simples de utilização nos passamos apenas um parametro de entrada,
que neste caso é o nome do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e
é com ele que trabalhamos então.

# OBS: Por padrão a função open() abre o arquivo para leitura. Este arquivo deve existir, ou teremos o erro
FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r = MOdo de leitura

"""

# Exemplo

arquivo = open('texto.txt', encoding='UTF-8')

# print(arquivo)
# print(type(arquivo))

# Para ler o conteudo de um arquivo, devemos utiizar a função read()

print(arquivo.read())

# OBS: o python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor funciona com
# o curso quando estamos ecrevendo.
