"""

Dunder Name e Dunder Main

Dunder = Doble Under

Dunder Name = __name__

Dunder Main = __main__

Em python são utilizados dunder para criar funções, tributos, propriedades, ... utilizando Double Under
para não gerar conflito com os nomes desses elementos na programção.

# Na linguagem C, temos um programa da seguinte forma:

    int main(){

    return 0;

}

# Na linga=uagem Java, temos um programa da seguinte forma:
    public static void main(string[] args){

}

# Em python, se executarmos um modulo python diretamente na linha de comando, internamente o python atribuirá
a variavel __name__ o valor __main__ indicando que este modulo é o modulo de execução principal.

==========================

from teste import numero_impar

print(numero_impar([1, 2, 3, 4, 5, 6, 7]))

"""

import primeiro, segundo

print(primeiro.__name__)


