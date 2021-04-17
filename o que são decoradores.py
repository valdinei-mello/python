"""
O que são decoradores ? Decorators

- Decorators são funções;
- Decorators envolve outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Highr Order Funcitions;
- Decorators tem uma sintaxe propria, usando "@" (Syntact Sugar / Açucar Sintatico)



/-----------------------------------------------------/
/        Function Decorator                           /
------------------------------------------------------


-------------------------------------------------------
/ /-----------------------------------------------------/ /
/ /               Função Decorada                      / /
/ /----------------------------------------------------/ /
/------------------------------------------------------/


+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Decorators  como funções (Sintaxe não recomendada / Sem açucar Sintatico)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você !')
        funcao()
        print('Tenha um otimo dia !')
    return sendo


def saudacao():
    print('Seja bem vindo')


# Testando 1:
resp = seja_educado(saudacao)
resp()
print('')
# Testando 2:


def raiva():
    print('EU TE ODEIO')


raiva_educada = seja_educado(raiva)
raiva_educada()


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Decorators com syntax sugar ( açucar sintatico)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você !')
        funcao()
        print('Tenha uma excelente dia !')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é VALDINEI')


@seja_educado_mesmo
def dormir():
    print('Quero dormir !')


# Testando 1:
apresentando()
print('')
dormir()



"""
"""
|------------------------------------------------------
| Home    | Serviços    | Produtos    | Administrativo|
-------------------------------------------------------

http://www.suaempresa.com.br/home
http://www.suaempresa.com.br/servicos
http://www.suaempresa.com.br/produtos
http://www.suaempresa.com.br/administrativo

# OBS: Não é codifo funcional, é apenas um exemplo;

def checa_login():
    if not request.usuario:
        redrect('http://www.suaempresa.com.br')
        
        
def home():
    return ("Pode acessar home")
    
def servicos():
    return ("Pode acessar serviços')
    
def produtos():
    retunr ("Pode acessar produtos')
    
@checa_login    
def admin():
    return ("Pode acessar Admin")

"""

# OBS: Não confunda decorator com decorators function


def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você !')
        funcao()
        print('Tenha uma excelente dia !')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é VALDINEI')


@seja_educado_mesmo
def dormir():
    print('Quero dormir !')


# Testando 1:
apresentando()
print('')
dormir()





