"""
Geradores

Geradores = são iterators (Iteradores);

OBS: O contrario não é verdadeiro, nen todo iterator é um generator.

Outras informações:
     - Generators podem ser criados com funções geradoras;
     - Funções geradoras utilzam a palavra reservada yield;
     - Generators poder ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions.

===================================================================================/
/Funções                                    /Generator Functions                   /
===================================================================================
/Utilizam return                            /Utilizam yield                        /
===================================================================================
/Retorna uma vez                            /Pode utilizar yield multiplas vezes   /
===================================================================================
/Quando executada retorna uma valor         /quanto executada retorna uma generator/
===================================================================================

"""

# Exemplo Generators Function (Função Geradora)
# OBS: Uma Generator Function não é um Generator. Ela gera um generator, ok!


def conta_ate(valor_max):
    contador = 1
    while contador <= valor_max:
        yield contador
        contador += 1


gen = conta_ate(5)

for num in gen:
    print(num)

