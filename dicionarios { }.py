"""

Dicionarios

OBS: Em alguns inguagens de programação, os dicionarios python são conhecidos por mapas.

Dicionarios são coleções do tipo chave/valor.

Dicionarios são representados por chaves {}.

OBS: Sobre dicionarios
    - Chave e valor são separados por dosi pontos ':';
    - Tanto chave, valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;


--------------------------------------------------------
# Criação de Dicionário
# Forma 1 (Mais comun)
paises = {'br': 'brasil', 'usa': 'estados unidos', 'py': 'paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos Comun)

paises = dict(br='brasil', usa='estados unidos', py='mexico')

print(paises)
print(type(paises))
-------------------------------------------------------------------

# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['usa'])


# Forma 2 - Acessando elemento via get - Recomendada
print(paises.get('br'))
print(paises.get('usa'))

pais = paises.get('br')

if pais:
    print(f"Encontrei o pais {pais.title()}!")
else:
    print("Não encontrei o pais !")


OBS: Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('r', 'Não encontrei o pais')
print(pais)

------------------------------------------------------------------
# Podemos verificar se determinada chave se encontra em um dicionario

print('br' in paises)
print('ru' in paises)
print('paraguai' in paises)

---------------------------------------------------------
# Podmos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla como chave de dicionarios
# Tupla são bastantes interessantes de serem utilizadas como chave de dicionarios, pois as mesmas são imutavies

localidades = {
    (13.342, 121.323): 'Tokio',
    (879.748, 178.741): 'Brasil',
    (745.254, 741.412): 'Mexico',
}

print(localidades)
print(type(localidades))
-------------------------------------------------------

#  Adicionar elementos em um dicionario

receita = {'janeiro': 100, 'fevereiro': 200, 'março': 300}
print(receita)
print(type(receita))

# Forma 1 - Forma mais comun
receita['abril'] = 400
print(receita)

# Forma 2
novo_dado = {'maio': 500}
receita.update(novo_dado)  # receita.update({'maio': 500})
print(receita)

# Atualizando dados um um dicionario

# Forma 1:

receita['maio'] = 550
print(receita)

# Forma 2:

receita.update({'maio': 600})
print(receita)

# Conclusão 1: A forma de adicionar elemntos ou atualizar dadso em um dicionario é a mesma.
# Conclusão 2: Em dixionarios, NÃO podemos ter chaves repetidas.
----------------------------------------------------------------------

# Remover dados de um dicionario
receita = {'janeiro': 100, 'fevereiro': 200, 'março': 300}
print(receita)

# Forma 1: (Mais Comun)
ret = receita.pop('março')
print(ret)
print(receita)

# OBS 1: Aqui precisamos sempre informar a chave do elemnto que desejamos remover
# OBS 2: Ao remover um objeto, o vamor deste objeto sempre é retornado.

# Forma 2:
del receita['fevereiro']
print(receita)

# OBS: Neste caso o valor removido não é retornado
-------------------------------------------------------------------------------------------------------
# Imagine que voce tenha um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.

Carrinhos de Compras:
    Produto 1:
        - Nome
        - quantidade
        - preço
    Produto 2:
        - Nome
        - quantidade
        - preço


# 1 - Poderiamos utilizar uma lista para armazenar as informações do produto

carrinho = []

produto1 = ['Playsation', 1, 2300.00]
produto2 = ['God of war', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada infomação no produto

# 2 - Poderiamos utilizar uma tupla

produto1 = ('Playtsation 4', 1, 2300.00)
produto1 = ('God of war 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada infomação no produto

# 3 - Poderiamos utilizar um dicionario

carrinho = []
produto1 = {'nome': 'Playstation', 'qtde': 1, 'valor': 2300.00}
produto2 = {'nome': 'God of war', 'qtde': 1, 'valor': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma facilmente adicionamos ou removemos produtos do carrinho
# e em cada produto podemos ter a certeza de cada informação
--------------------------------------------------------

# Metodos de dicionarios.

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionario (Zerar dados)
d.clear()
print(d)

# Copiando um dicionario para outro
# Forma 1: Deep copy
novo = d.copy()
print(novo)

novo['d'] = 4
print(novo)

# Forma 2: Shallow copy
novo = d
print(novo)
novo['d'] = 4

print(d)
print(novo)


"""


# Forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'email', 'endereço', 'telefone'], 'desconhecido')
print(usuario)

# O metodo fromkeya recebe dois parametros: um interável e outro valor.
# Ele vai gerar para cada valor interavel  uma chave  e irá atribuir a esta chave o valor informado.

usuario['nome'] = 'valdinei'
print(usuario)

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 10), 'valor')
print(veja)


