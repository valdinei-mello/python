"""
teste de memoria com generators

# Seguencia de Fibonati: 1 ,1, 2, 3, 5, 8, .....

=====================

# Função usando listas (1.047,4MB)
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


for n in fib_lista(100000):
    print(n)

"""


# Função usando geradores(588,5MB)
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1


for n in fib_gen(100000):
    print(n)





