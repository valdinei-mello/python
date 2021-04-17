"""
modulo collections - default dict

# recapitulando dicoinario

dicionario = {'curso': 'programação em python'}
print(dicionario)
print(dicionario['curso'])
-------------------------------------

Default Dict = ao criar um dicionario utilizando-o, nos informamos um valor default,
podendo utilizar um lambda para isso, este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar um chave que não exista,
esse chave será criada e o valor default será atrinuido

OBS: lambda são fucnções sem nome que podem ou não receber parametros de entrada e retornar valores;

"""

from collections import defaultdict

dic = defaultdict(lambda: 0)
dic['curso'] = 'python'
print(dic['curso'])
print(dic['outro'])  # se fosse um dicionario simples geraria um erro, porem aqui retorno o lambda
print(dic['curso'])



