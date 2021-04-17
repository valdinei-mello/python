"""
POO - Objetos

Objetos = São instacias das classes, ou seja, após o mapeamento do objeto do mundo real para sua
representação computacionais, devemos poder criar quantos objetos forem necessa´rios. Podemos pensar
nos objetos;instancias de uma classe como variaveis do tipo definido na classe.

===================
# Instâncias/Objetos Lâmpada
lamp1 = Lampada('branca', 110, 60)

cc1 = ContaCorrente(5000, 20000)

user = Usuario('valdnei', 'mello', 'valdinei.mello.22@gmail.com', '1452')

print(lamp1.checa_lampada())

"""


class Lampada:

    def __init__(self, cor, volts, luminosidade):
        self.__cor = cor
        self.__volts = volts
        self.__luminosidade = luminosidade
        self.__ligada = False

    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

    def checa_lampada(self):
        if self.__ligada:
            return f'Lâmpada ligada !!!'
        return f'Lâmpada desligada !!'


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O clinte {self.__nome} diz oi !')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é o {self.__cliente._Cliente__nome}')


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instâncias/Objetos Lâmpada
cli_1 = Cliente('valdinei', "395.147.125-2")

cc = ContaCorrente(5000, 10000, cli_1)

cc.mostra_cliente()

