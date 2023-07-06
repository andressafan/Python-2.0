# Tuplas

# toda variável "declarada" (em python não se declara variáveis)
# recebe um espaço na memória

# lanche = hambúrguer
# lanche recebe hambúrguer           espaço na memória: [hambúrguer]

# lanche = suco
# lanche recebe suco                 espaço na memória: [suco]
# a memória é trocada

# como criar uma variável com mais de um espaço:
# lanche
# [🍔] variável simples
# lanche
# [🍔][🥤][🍕][🍮] variável composta

# 3 tipos de variáveis compostas:
# Tuplas
# Listas
# Dicionários

# Tuplas:
# variável que guarda vários valores

# Como acessar o elementos de uma tupla?
# lanche
# [🍔][🥤][🍕][🍮]
# [ 0 ][1][ 2 ][3]
# [-4 ][-3][-2][-1]
# cada elemento tem um índice


# print(lanche[2]) --> 🍕
# print(lanche[0:2]) --> 🍔🥤 (em um fatiamento o último elemento é ignorado)
# print(lanche[1:]) ---> 🥤🍕🍮 ( vai do índice [1] até o final
# print(lanche[-1]) --> 🍮 (conta na ordem inversa)
# len(lanche) ---> 4      len = lenght = comprimento diz quantos elementos tem

# for c in lanche:            # lanche              c  --> variável simples
#   print(c)                  # [🍔][🥤][🍕][🍮]   [🍔]   c percorre a tupla item por item
#                                                   [🥤]
#                                                   [🍕]
#                                                   [🍮]

# "As tuplas são IMUTÁVEIS!!!"

# lanche
# [🍔][🥤][🍕][🍮]
# não tem como mudar um item de uma tupla
