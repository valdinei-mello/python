"""
POO - Atributos

Atributos = Representam as caracteristicas do objeto, ou seja, pelo atributos nos conseguimos representar
computacionalmente os estados de um objeto.

Em python dividimso os atributos em 3 grupos:
    Atributos de instancia;
    Atributos de classe;
    Atributos dinâmicos;

# Atributos de instancia: São atributos declarados dentro do metodo construtor.

OBS: Metodo construtor: è um metodo especial utilzado para a construção do objeto.


# Em Java uma classe Lampada incluindo seus atributos, ficaria mais ou menos:

public class Lampada(){
    private int volts;
    public String cor;
    protected Boolean ligada;

    public Lampada(int volts, String cor){
        this.volts = volts;
        this.cor = cor;
    }
}


EM python por convenção ficou estabelecido que todo atributo de uma classe é public, ou seja, pode ser acessado
em todo o projeto, Caso queiramos demostrar que determibado atributo deve ser tratado como privado, ou seja, que deve
ser acessado/utilizado somente dentro da propria classe onde está declarado, utiliza - se __ dupla underscore no
inicio do seu nome.

Isso é conhecido tambem como Name Mangling.

==================

# Classes com atributo de instanca publico


class Lampada:
    def __init__(self, volts, cor):
        self.volts = volts
        self.cor = cor
        self.igada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos publicos e Atributos privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


OBS: Lembre se que isso é apenas uma convenção, ou seja, a linguagem python não vai impedir  que façamos acesso aos
atributos sinalizados como pric=vados fora da classe


# Exemplos

user = Acesso('valdinei.mello.22@gmail.com', 'gdenkl')
print(user.email)
# print(user.senha)  # AttributeError

print(user._Acesso__senha)  # Temos acesso, mais não deveriamos fazer este acesso (Name Mangling)
user.mostra_senha()
user.mostra_email()

# O que significa atributos de instancia ?
# Significa que ao criarmos instacias de uma classe, todas as instancias terão estes atribustos.

user1 = Acesso("hhhh@gmail.com", 'aasndk')
user2 = Acesso('hffg@gmail.com', 'hdgfv')

user1.mostra_email()
user2.mostra_email()

=======================================

# Atributos de Classe


# Atributos de classe, são atributos, claro, que são declarados diretamente na classe , ou seja, fora do construtor.
# Geralemnete já inicializamos um valor , e este valor é compartilhado entre todas as instancias da classe.
# Ou seja, ao invés de cada instancia da classe ter seus proprios valores como é o caso dos atributo de instancia,
# com os atributos de classe todas as instancias terão o mesmo valor para este atributo.

# Refatorar a classe produto


class Produto:

    # Atributo de classe

    imposto = 1.05  # 0,05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto("aps4", 'video game', 2300)
p2 = Produto('xbox', 'video game', 4500)

print(p1.valor)  # Acesso possivél, mais incorreto
print(p2.valor)


# OBS: Não precisamos criar uma instancia de uma classe para fazermos aceso a um atributo de classe

print(Produto.imposto) # Acesso correto de uma atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguaguans como o java, os atributos conhecidos como atributos estaticos ce classes aqui em python são
# chamados  de atributos estáticos;



"""

# Classes com atributo de instanca publico


class Lampada:
    def __init__(self, volts, cor):
        self.volts = volts
        self.cor = cor
        self.igada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Atributos Dinâmicos: Um atributo de instancia que pode se criado em tempo de execução.

# OBS: O atributo dinamico será exclusivo da instancia que o criou.

p1 = Produto("ps4", "video game", 2300)
p2 = Produto('xbox', 'video game', 3000)

# Criando um atributo dinamico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso

print(f"Nome: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}")
# print(f"Nome: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}")

# Deletando atributos
print(p1.__dict__)
print(p2.__dict__)

del p2.peso
del p2.valor

print(p1.__dict__)
print(p2.__dict__)



