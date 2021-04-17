"""
POO - Métodos

 - Métodos (funções) = Representam os comportamento dos objetos, ou seja, as ações que este objeto podem realizar
 no seu sistema.

 Em python dividimos os metodos em dois grupos:
 - Métodos de instancia;
 - Métodos de classe;

# Métodos de instancia

# O método dunder __init__ é um método especial chamado de construtor e
 sua função é construir o objeto a apartir da classe.

 OBS: Todo elemnto em pyrthon que inicia/finaliza com duplo underline é chamado de dunder ( Double underline).

 OBS: Os métodos dunder em python são chamados de métodos mágicos

 ATENÇÂO: Por mais que possamos criar nossas proprias funções utilizando dunder não é aconselhado.
 Python possui varios métodos com essa nomenclatura e pode se que mudemos o comportamento dessas funções magicas
 interna da linguagem então eite ao maximo, de preferencia nunca faça.

 # Métodos são escritos em letras minusculas, se o nome for composto será separado por underline

=================================

p1 = Produto('ps4', 'video game', 3000)
print(p1.desconto(20))

u1 = Usuario('valdinei', 'mello', 'valdinei.mello.22@gmail.com', 'fmverknvjfn')
print(u1.nome_completo())
print(Usuario.nome_completo(u1))

=============================



"""


class Lampada:
    def __init__(self, cor, volts, luminosidade):
        self.__cor = cor
        self.__volts = volts
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorno o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return f'{self.__nome}  {self.__sobrenome}'

    def checa_senha(self, senha):
        if senha == self.__senha:
            return True
        return False


nome = input("Informe o nome: ")
sobrenome = input("Informe o sobrenome: ")
email = input("Informe o email: ")
senha = input("Informe a senha: ")
confirma_senha = input("Confirme a senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print("Senha não confere !")


print('Usuario criado com sucesso!')
senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido !')
else:
    print('Acesso negado !')

















