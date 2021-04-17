"""
Estruturas Logicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not;
Operadores binários:
    -and, or, is;

Regras de funcionamento:

Para o 'and' ambos os valores precisam ser 'true'
Para o 'or' um dos valores precisam ser 'true'
Para o 'not' o valor do booleano é invertido
Para o 'is' o valor é comparado com um segundo
"""
ativo = False
logado = False

# Se não estiver ativo
if ativo is True:
    print("Voce precisa ativar a sua conta!")
