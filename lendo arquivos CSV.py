"""
Lendo arquivos CSV

CSV - Coma Separated Values - Valores Separados por Virgula

==============================================
# Separador por virgula

1, 2, 3, 4

"valdinei", "mello"
============================================

# Sepador por ponto e virgula

1; 2; 3; 4

"valdinei"; "mello"
======================================

# Sepador por ponto e virgula

1 2 3 4

"valdinei" "mello"
============================================

https://dados.gov.br/dataset

=========================

# Possivel de se trabalhar, mas não é o ideal (Trabalhoso)

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)


Alinguagem python, possui duas fomras diferentes para ler dados em aqrquivos csv:
    - reader - permite que iteremos sobre as linhas do arquivo CSV como lists;
    - dictreader - permite que iteremos sobre as linhas do arquivo CSV como OrderDicts;


===========================

# REader

from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pula o cabeçalho
    for linha in leitor_csv:
        #  cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} em centimetros')


# DictReader

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        #  cada linha é um orderedict
        print(f"{linha['Nome']} nasceu em {linha['Pais']} e mede {linha['Altura (em cm)']} em centimetros")

"""

# DictReader com outro separador

from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        #  cada linha é um orderedict
        print(f"{linha['Nome']} nasceu em {linha['Pais']} e mede {linha['Altura (em cm)']} em centimetros")


