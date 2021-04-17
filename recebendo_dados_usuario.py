"""

Recebendo dados do usuario

input() = Todo dado recebido via input é do tipo string

Em pythom string é tudo que estiver entre:
 - Aspas Simples;
 - Aspas Duplas;
 - Aspas simples triplas;
 - Aspas duplas triplas;
 
 Exemplos:
  - Aspas Simples = 'Valdinei';
 - Aspas Duplas = "Valdinei" ;
 - Aspas simples triplas = '''Valdinei''';
 """
 #- Aspas duplas triplas = """Valdinei""";
 


# Entrada de dados #

nome = input("Qual seu nome ?") # input = entrada

# Exemplo de print antigo
# print('Seja bem vindo %s' % nome)

# Exemplo de print moderno
# print("Seja Bem Vindo {0}".format(nome))

# Exemplo de print mais atual
print(f"Seja Bem Vindo {nome}")

print("Qual a sua idade?")
idade = input()



# Processamento #


# Saída de dados #

# Exemplo de print antigo
# print("O %s tem %s anos" % (nome, idade))

# Exemplo de print moderno
# print("O {0} tem {1} anos".format(nome, idade))

# Exemplo,de print mais atual
# print(f"O {nome} tem {idade} anos")

"""

Cast é a conversão de um tipo de dado para outro

"""
print(f"O {nome} nasceu em {2020-int(idade)} e tem {idade} anos")
