# Listas

# Tuplas ()
# Lista []

# listas permitem uma manipulação maior dos elementos
# elas são mutáveis!

# lanche = ['🍔', '🥤', '🍕', '🍮']

# lanche:
# [🍔][🥤][🍕][🍮]
# [ 0 ][1][ 2 ][3]

# lanche[3] = '🍨'

# lanche:
# [🍔][🥤][🍕][🍨]
# [ 0 ][1][ 2 ][3]

# Adicionando elementos:

# lanche.append('🍪')

# lanche:
# [🍔][🥤][🍕][🍨][🍪]
# [ 0 ][1][ 2 ][3][ 4 ]

# Adicionando elementos em posições:

# lanche.insert(0, '🌭')

# lanche:
# [🌭][🍔][🥤][🍕][🍨][🍪]
# [ 0 ][1][ 2 ][3][ 4 ][5]

# Apagando elementos:

# del lanche[3]
# ou
# lanche.pop(3)
# ou
# lanche.remove('🍕')

# lanche:
# [🌭][🍔][🥤][🍨][🍪]
# [ 0 ][1][ 2 ][3][ 4 ]

# lanche.pop()   ---> sem parâmetro remove o último índice

# lanche:
# [🌭][🍔][🥤][🍨]
# [ 0 ][1][ 2 ][3]

# caso você tente remover um item que não está na lista
# o programa vai gerar um erro

# Como verificar se um elemento está na lista?

# if '🍕' in lanche:
#   lanche.remove('🍕')  ---> remove a pizza se ela está na lista

# Criar listas através de estruturas de repetição

# valores = list(range(4, 11))

# valores:
# [4][5][6][7][8][9][10]
# [0][1][2][3][4][5][ 6 ]

# valores = [8, 2, 5, 4, 9, 3, 0]

# valores:
# [8][2][5][4][9][3][0]
# [0][1][2][3][4][5][6] --> índices

# valores.sort() ---> ordena os valores

# valores:
# [0][2][3][4][5][8][9]
# [0][1][2][3][4][5][6]

# valores.sort(reverse = True) --> ordena na ordem decrescente

# valores:
# [9][8][5][4][3][2][0]
# [0][1][2][3][4][5][6] 

# len(valores) --> comprimento da lista (7)



