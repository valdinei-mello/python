"""
Loop_While

Forma geral:

while expressão booleana:
    //execução do loop


O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num <5
--------------------------------------------------------
# Exemplo 1:
num = 1

while num <= 10:
    print(num)
    num += 1

# OBS: Em um loop while é importante que cuidemos do critério de parada
-----------------------------------------------------------
# Exemplo 2:
resp = ""

while resp != "sim":
    resp = input("Ja acabou ? ")

    if resp == "sim":
        print("PARABÉNS, VOCE ACABOU !!! \U0001F64C")


# OBS: Em um loop while é importante que cuidemos do critério de parada


"""

resp = ""

while resp != "sim":
    resp = input("Ja acabou ? ")

    if resp == "sim":
        print("PARABÉNS, VOCE ACABOU !!! \U0001F64C")


# OBS: Em um loop while é importante que cuidemos do critério de parada
