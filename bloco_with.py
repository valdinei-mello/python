"""
O bloco with

# 1 - Abrir o arquivo;
# 2 - Trabalhar o arquivo;
# 3 - Fechar o arquivo;

O bloco with é utilizado para criar um contexto de trabalho, onde os recurso utilizados são fechados
após o bloco with.


"""


# o bloco with - forma pythonica de manipular arquivos

with open('texto.txt', encoding='utf-8') as arquivo:
    print(arquivo.read())

    print(arquivo.closed)

print(arquivo.closed)

