"""
Escrevendo_CSV

reader() (leitor); writer() (escrever)

writerow() - escreve uma linha
================

# writer() = gera um objeto para que possamos escrever em um arquivo csv.
# Utilizamos o método writerow() para escrever cada linha.
# Esse método recebe uma lista.



from csv import writer

with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duração'])
    while filme != 'sair':
        filme = input("Informe o nome do filme: ")
        if filme != 'sair':
            genero = input('Informe o genero do filme: ')
            duracao = input('Informe a duração em minutos do filme: ')
            escritor_csv.writerow([filme, genero, duracao])




"""


# DicWriter
# Obs: As chaves devem ser as mesmas utilizadoas no cabeçalho

from csv import DictWriter

with open("filmes.csv", 'w') as arquivo:
    cabecalho = ['Titulo', "Genero", "Duracao"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input("Informe o nome do filme: ")
        if filme != 'sair':
            genero = input("Informe o genero: ")
            duracao = input("Informe a duração: ")
            escritor_csv.writerow({'Titulo': filme, 'Genero': genero, 'Duracao': duracao})






