"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura não podemos relaizar a escrita nele, apenas ler.
Da mesma forma que não podemos ler um arquivo aberto p\ra escrita.

# OBS: Ao abrir uma arquivo para escrita, o arquivo é criado pelo Sistema Operacional.

PAra escrever dados em um arquivo, após abrir um arquivo utilizamos a função write().

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado um novo arquivo, caso exista um
aequivo com o mesmo nome , ele irá sobreescrever o mesmo.

=======================

# Exemplo de escrita - modo 'w' - write (escrita)

with open('texto.txt', 'w', encoding='utf-8') as arq:
    arq.write('programação é muito facil...')

with open('texto.txt', encoding='utf-8') as arq:
    print(arq.read())


"""

with open('frutas.txt', 'w', encoding='utf-8') as arq:
    while True:
        fruta = input('Digite uma fruta ou sair para finalizar: ')
        if fruta != 'sair':
            arq.write(fruta + '\n')
        else:
            break


