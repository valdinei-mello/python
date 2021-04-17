"""
Documentando funções com Docstrings

OBS: podemos ter acesso a documentação de em python utilizando a propriedade especial __DOC__

Podemos ainda fazer acesso a documentação com a função help()
"""

# Exemplos
from builtins import print


def diz_oi():
    """Uma função simples que retorna a string 'OI' """
    return 'oi'


def exponencial(numero, potencial=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' á 'potencia' informada
    :param numero: Numero que desejamos gerar o exponencial;
    :param potencial: Potencia que queremos gerar o exponencial, por padraão é 2;
    :return: Retorna o exponencial de "numero' por 'Potencia'
    """
    return numero ** potencial


print(exponencial(7))

