# Dicionários
# índices literais/ personalizáveis

# tuplas ()
# listas []
# dicionários {}

# dados = dict()
# dados = {'nome':'Pedro', 'idade':25}

#  dados:
# ['Pedro'] [25]
# [  nome ][idade] # você pode nomear os índices

# print(dados['nome']) ---> 'Pedro'
# print(dados['idade']) ---> 25

# Adicionar elementos:

# dados['sexo'] = 'M'

#  dados:
# ['Pedro'] [25]  ['M']
# [  nome ][idade][sexo]

# Remover elementos:

# deldados['idade']

#  dados:
# ['Pedro']['M']
# [  nome ][sexo]

# filme = {'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'}

# filme:
# ['Star Wars'][1977]['George Lucas'] --> values/valores
# [  titulo   ][ ano][    diretor   ] ---> keys/chaves

# print(filme.values()) --> retorna todos os valores do dicionário
# print(filme.keys()) ---> retorna as chaves
# print(filme.items()) --> pega tanto os valores quanto as chaves


# Em laços de repetição:

# for k, v in filme.items():  --> para cada chave(k) e valor (v) em filme.items
#   print(f'O {k} é {v}') ---> O titulo é Star Wars ... O ano é 1977 ... O diretor é George Lucas


# Juntando listas, tuplas e dicionários:

# locadora = list()
# locadora.append(filme)

# locadora:
# [     [ 'Star Wars' ][ 1977 ][ 'George Lucas' ]     ][     [ 'Avengers' ][ 2012 ][ 'Joss Whedon' ]     ][     [ 'Matrix' ][ 1999 ][ 'Wachowski' ]     ]
#       [    titulo   ][ ano  ][    diretor     ]            [   titulo   ][ ano  ][    diretor    ]            [   titulo ][ ano  ][   diretor   ]
# [                        0                          ][                    1                            ][                       2                     ]

# print(locadora[0]['ano']) ---> 1977
# print(locadora[2]['titulo']) ---> 'Matrix'



