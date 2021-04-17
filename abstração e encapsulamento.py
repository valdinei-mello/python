"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular o codigo dentro de um grupo lógico e hierarquico utilizando classes.

Encapsular = Cápsula



            classe
---------------------------------------------
/                                            /
/             atributos e métodos            /
/____________________________________________/

# Relambrando Atributos/Métods privados em python

Imagine que temos uma classe chamdad pessoa, contendo um atributo
chamado __nome e um método privado chamado __falar()

Esses elementos privados só devem/devriam ser acessados dentro da classe. Mas o
python não bloqueia este acesso fora da classe. Com python não  acontece um fênomeno
chamdo Nsme Mangling, que faz uma alteração na forma de se acessar os elemntos privados, conforme :

_Classe__elemento

Exemplo: Acessando elemntos privados fora da classe:

instância._Pessoa__nome

Instância._Pessoa__falar()


Abstração, em POO é o ato de expor apenas dados relevantes de uma classe , escondendo atributos e métodos
privados de usuario.





"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de R${self.__saldo} do titular {self.__titular} com limite de R${self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Você fez um deposito de R$:{valor} e seu saldo agora é de R$:{self.__saldo}")
        else:
            print('Você não pode depositar uma valor menor que zero.')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print(f'Você sacou R$:{valor} e agora tem R${self.__saldo}')
            else:
                print(f'Saldo insuficiente !')
        else:
            print(f'Você não pode sacar um valor negativo !')

    def transferir(self, valor, conta_destino):
        #  1 - Remover o valor da conta de origem
        self.__saldo -= valor

        # 2 - Adicionar o valor na conta de destino:
        conta_destino.__saldo += valor

# Testando


conta1 = Conta('valdinei', 100.00, 2000.00)
conta1.extrato()

conta2 = Conta('marcos', 700.00, 8000.00)
conta2.extrato()


conta1.transferir(100, conta2)

conta1.extrato()
conta2.extrato()






