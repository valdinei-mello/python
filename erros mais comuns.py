"""
Erros mais comuns

É importante prestar atenção e aprender a ler as saídas de rros geradas pela execução de nosso código;

Os erros mais comuns:

1 -SyntaxError: Ocorre quando o python encontra um erro de sistaxe.

# Exemplos SyntaxError

a) def função:
    print("valdinei")

b) None = 1

c) return

=======================================================================

2 - NameError: Ocorre quando uma variavle ou função não foi definida.

# Exemplos NameError

a) print(valdnei)

b) geek()

c)

a = 18

if a < 10:
     msg = 'é maior que 10'
print(msg)

3 - TypeError: Ocorre quando uma função/operação/ação é aplicada a um tipe errado.

# Exemplos TypeError

a) print(len(5))

b) print('valdinei' + [])

==========================================================

4 - IndexError: Ocorre quando tentamos acessar um elemnto em uma lisya ou outro tipo de dado indexado utilizando
um indice inválido;

# Exemplos IndexError

a) lista = ['valdinei']
   print(lista[10])

========================================================

5 - ValueError: Ocorre quando uma operação/função built-in (integrada) recebe uma argumento com tipo correto ,
,mas valor inapropriado.

# Exemplos ValueError

a) print(int('ney'))

=========================================================

6 - KeyError: Ocorre quando tentamos acessar um dicionario com uma chave que não existe.

# Exemplos KeyError

a) dic = {'a': 1, 'b': 3}
   print(dic['c'])

====================================================

7 - AttributeError: Ocorre quando uma variavel não tem um atributo ou função.

# Exemplos AttributeError

a) tupla = (1, 25, 254, 258)
   print(tupla.sort())

   ===================================================

8 - IndentetionError: Ocorre quando não respeitamos a indentação do python ( 4 espaços).

Exemplos IndentetionError

a)  def nova():
    print('ney')




OBS: Execptions e Erros são sinonimos  na programação.

OBS: Importante ler e prestar atenção na saída de erro.

"""












