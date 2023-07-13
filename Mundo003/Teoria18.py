# Listas
# Parte 2

# dados
# ['Pedro'][25]
# [   0   ][ 1 ]

# dados = list()
# dados.append('Pedro')
# dados.append(25)
# print(dados[0])
# print(dados[1])


#  pessoas --> o primeiro elemento é uma lista
#       lista            lista            lista
# [ ['Pedro'][25] ][ ['Maria'][19] ][ ['João'][32] ]
#   [   0   ][ 1 ]   [   0   ][ 1 ]   [   0  ][ 1 ]
# [       0       ][        1      ][       2      ]


# pessoas = list()
# pessoas.append(dados[:]) adiciona uma cópia da lista dados


# pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

# print(pessoas[0][0]) ---> 'Pedro'
# print(pessoas[1][1]) ---> 19
# print(pessoas[2][0]) ---> 'João'
# print(pessoas[1]) ---> ['Maria', 19]
