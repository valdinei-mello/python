"""
Criando sua propria versão de loop

========================================

for num in [1, 2, 3, 4]:
    print(num)

for letra in 'valdinei':
    print(letra)

iter([1, 2, 3, 4])
iter('valdinei')


"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('valdinei de mello')

