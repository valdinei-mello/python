"""
Seek e Cursors

Seek() - é utilizada para movimentar o cursor pelo arquivo.


================

arquivo = open('texto.txt', encoding='utf-8')
print(arquivo.read())


# A função seek() é utilizada para movimentação do cursor pelo arquivo,
# ela recebe um parametro que indica onde queremos colocar o cursor.

# Movimentando o curso pelo arquivo com a função seek()
arquivo.seek(10)
print(arquivo.read())

===================

arquivo = open('texto.txt', encoding='utf-8')

# readline() = Função que lê o arquivo linha a linha

ret = arquivo.readline()
print(type(ret))

print(ret.split(' '))

============

arquivo = open('texto.txt', encoding='utf-8')

# readlines()

linhas = arquivo.readlines()
print(linhas)
print(len(linhas))

=======================

# OBS: Quando abrimos o arquivo com a função open(), é criado uma conexão entre o arquivo no disco é o programa.
# Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o qrquivo devemos fechar essa conexão.
# Para  isso utilizamos o comando close().

# 1 - Abrir o arquivo;

arquivo = open('texto.txt', encoding='utf-8')

# 2 - Trabalhar o arquivo;

print(arquivo.read())
print(arquivo.closed)  # Verifica se o arquivo esta aberto ou fechado

# 3 - Fechar o arquivo;

arquivo.close()
print(arquivo.closed)  # Verifica se o arquivo esta aberto ou fechado


# OBS: Se tentarmos manupular um arquivo após seu fechamento, teremos um valueerror


"""

# Com a função read(), podemos limitar a qtde de caracteres a ser lido

arquivo = open('texto.txt', encoding='utf=8')
print(arquivo.read(5))
