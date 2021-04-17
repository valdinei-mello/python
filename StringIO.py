"""
StringIO

ATENÇÂO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa ter permissão:
    - Permissão de leitura;
    - Permissão de escrita;

StringIO = Utilizado para ler e criar arquivos em memoria.
"""

# Primeiro fazemos o import
from io import StringIO

msg = 'String normal'

# Podemos criar um arquivo em memoria, já com uma string inserida ou mesmo vazio
arquivo = StringIO(msg)
# arquivo = open('arquivo.txt', 'w')

# Agora tendo o arquivo, podemo utilizar tudo que já sabemos
print(arquivo.read())
arquivo.write('outro texto')
arquivo.seek(0)
print(arquivo.read())

