"""
POO  -  Herança ( Inheritance)

A ideia de herança é a de reaproveitar codigo. Tambme extender nossas classes.

OBS: Com a herança, apartir de uma classe existente, nós extendemos outra classe que passa
a herdar atributos e metodos da classe herdada.

Cliente:
    -nome;
    -sobrenome;
    -cpf;
    renda;

Funcionario:
    -nome;
    -sobrenome;
    -cpf;
    matricula;

================================================================

PERGUNTAR: Existe alguma entidade generica o suficiente para
encapsular os atributos e metodos comuns a outras entidades ?

class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Fucionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matriucla = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('valdinei', 'mello', '321.321.654-90', 5000.00)
print(cliente1.nome_completo())

funcionario1 = Fucionario('jorge', 'garcia', '321.147.582-58', 002864j)
print(funcionario1.nome_completo())



OBS: Quando uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe a classe herdada é conhecida por:

    [Pessoa]
    -SuperClasse;
    -Classe mãe;
    -Classe pai;
    -Classe base;
    -Classe generica;

Quando uma classe herda de outra classe ela é chamada :
    [Cliente, Funcionario]
    -Sub classe;
    -Classe filha;
    -Classe especifica;

=================================================

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    #  Cliente herda Pessoa
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Não é uma forma comun de se fazer a declaração de herança
        self.__renda = renda


class Fucionario(Pessoa):
    #  Funcionario herda Pessoa
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma correta de se fazer a declaração de herança
        self.__matriucla = matricula


cliente1 = Cliente('valdinei', 'mello', '321.321.654-90', 5000.00)
print(cliente1.nome_completo())

funcionario1 = Fucionario('jorge', 'garcia', '321.147.582-58', 002864j)
print(funcionario1.nome_completo())

print(funcionario1.__dict__)
print(cliente1.__dict__)

====================================================================================

# Sobrescrita de métodos (Overriding)

Ocorre quando sobrescrevemos/reiplementamos um método presente na super classe em classes filhas.
"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Não é uma forma comun de se fazer a declaração de herança
        self.__renda = renda


class Fucionario(Pessoa):
    """Funcionario herda Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma correta de se fazer a declaração de herança
        self.__matriucla = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'{self.__matriucla} {self._Pessoa__nome}'


cliente1 = Cliente('valdinei', 'mello', '321.321.654-90', 5000.00)
funcionario1 = Fucionario('jorge', 'garcia', '321.147.582-58', 002864j)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


