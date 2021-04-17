"""
POO - Classes

Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que voce queire fazer um sistema para automatizar as lampadas da sua casa.

Classes podem conter:
    - Atributos = Representam as caracteristicas do objeto, ou seja, pelo atributos conseguimos
    representas comutacionalmente. No caso da lampada, posivelmente iriamos querer saber se a lampada é
    110 ou 220 volts, se ela é branca ou amarela, vermelha ou outra cor, qual é a luminosidade dela etc

    - Metodos (funções) = Representam os comportamentos doobjeto, ou seja,
    as ações que este objeto pode relaizar no sistema. No caso da lampada, por exemplo, um comportamento comun que muito
    provavelmente iriamos querer representar no nosso sistemaé o de ligar/desligar.


Em python para definir uma classe utilizamos uma palavra reservada "class'.

OBS: Utilizamos a palvra pass, quando temso um bloco de codigo que ainda não esta implementado.

OBS: Quando nomeamos nossas classes em python utilizamos por convenção o nome com inicial em MAIUSCULO.
Se o nome for composto utilizamos as inicias de ambas as palavras em Maisculo, todas juntas.

Dica: Em computação não utilizamos caracteres especiais.

OBS: Quando estamos planejando um sw e definimos quais classes teremos no sistemas,
chamamos estes objetos que serão mapemados para a classes de entidades.

"""


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


lamp = Lampada()
print(type(lamp))





