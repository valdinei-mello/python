"""
Por que testar codigo ?

Testes automatizados !

          Aplicação Web
----------------------------------
/        frontedn e backend       /
----------------------------------
/         testes automatizados    /
----------------------------------

Por que testar codigo ?
    - reduzir bugs no codigo existente;
    - testes garantem que novo recursos da sua aplicação não alterem recursos antigos;
    - testes garantem que bugs ou seja problemas que foram corrigidos anteriormente continuem corrigidos;
    - testes garantem que a refatoração que costumamos a fazer não tragam novos bugs;

TDD - Test Driven Development (Desenvolvimento Guiado por Testes)

Com o TDD é utilizado estágios de desenvolvimento:
     - Você esceve seu teste primeiro;
     - Então você escreve o codigo minimo suficiente para fazer o teste passar ( ou seja, executar com sucesso);
      - Então refatora o codigo para relalizar a funcionalidade e tsta novamente;
      - Uma vez que o teste passe o recurso e considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - red;
    - green;
    - refactor;



"""


class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando ...')



tom = Gato("TOM")

print(tom.nome)
tom.miar()
