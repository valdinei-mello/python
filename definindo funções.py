"""
Definindo funções

 - funções são pequenos trechos de codico que realizam tarefas especificas;
 - pode ou não receber entradas de dados e retornar uma saida de dados;
 - muito uteis para executar procedimentos similares por repetidas vezes;

 OBS: se voce escrever uma função que realiza varias tarefas dentre dela
 e bom fazer uma verificação para que a função seja simplificada;

 ja utilizamos varias funções, desde que iniciamos o curso:
    - print()
    - len()
    - max()
    - min()
    - count()
    - e muita outras;



"""

# exemplo de utilização de funções

# cores = ['verde', 'azul', 'amarelo', 'branco']

# utilizando funções integrada (built-in) do python print()

# print(cores)

# curso = 'programação em python'
# print(curso)

# cores.append('roxo')
# print(cores)

# cores.clear()
# print(cores)

# DRY - don't repeat tourself - não repetiva você mesmo

# mas então, como definir funções ?
"""
em python a forma geral de definir uma função é:

def nome_da_função(parametro_de_entrada):
    blodo de função
    
Onde:
- nome da função =  sempre com letras minusculas e se for nome composto separado por underline (snake case);
- parametros de entrada =  são opcionais onde tendo mais de um ,cada um separado por virgula, podendo ser opcionais ou não;
bloco da função =  tambem chamdo de corpo da função ou implementação e onde o prcessamento da função acontece, 
neste bloco pode ter ou não retorno da função;

OBG: veja que para definir uma função, utilizamos a palavra reservada 'DEF' informando ao python que estamos
definindo uma função. Também abrimos o bloco de codigo com o já conhecido dosi pontos ':' que é utilizado em python 
para definir blocos

"""
# definindo função:
# exeplo 1:


def diz_oi():
    print('oi')


"""
OBS:
1 - veja que dentro das nossas funções podemos utilizar outras funções;
2 - veja que nossa função so executa uma tarefa, ou seja, veja que ela apenas diz 'oi';
3 - veja que esta função não recebe nenhum parametro de entrada;
4 - veja que esta função não retorna nada;

"""

# utilizando funções
# OBS: atenção nuca esqueça o parênteses ao executar uma função;

diz_oi()

# exemplo 2:


def cantar_parabens():
    print('parabens')
    print('muitas felicidades')
    print('saude')


for n in range(5):
    cantar_parabens()
    print('--------------')


# EM python podemos inclusive criar variaveis do tipo função e executar esta função através da variavél
canta = cantar_parabens
canta()








