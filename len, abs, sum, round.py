"""
Len, ABS, Sum , Round

# Len() = Retorna o tamanho ( ou seja, o numero de itens de um iteravél);

print(len("valdinei de mello"))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

# Por debaixo dos panos, quando utilizamos a função len() o python faz o seguinte:
# Dunder len
print('valdinei'.__len__())

------------------------------------------------------------

# ABS() = Retorna o valor absoluto de um numero inteiro ou rela. De forma básica seria o seu valor real sem sinal;

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

-----------------------------------------

# Sum() = Recebe como parametro um iteravél, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial.

# OBS: o valor inivial default é ZERO

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([1.2, 1.7]))
print(sum((1, 2, 3, 4)))
print(sum({1, 2, 3, 4}))
print(sum({'a': 1, 'b':  2, 'c':  3, 'd':  4}.values()))

------------------------------------------------------------------

Round() = Retorna um numero arredondado para n digito de precisão após a casa decimal.  Se a precisão não for informada,
retorna o inteiro mais proxima da entrada;

print(round(10.2))
print(round(10.5))
print(round(10.1))
print(round(10.9))
print(round(10.22518741, 2))

"""











