# Em python você pode iniciar uma variável composta de três maneiras
# (tupla), [lista], {dicionário}
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')  # pode ultilizar ou não os parênteses
print(lanche)

print(lanche[0])
print(lanche[1])
print(lanche[2])
print(lanche[3])

print('De trás pra frente: ')

print(lanche[-4])
print(lanche[-3])
print(lanche[-2])
print(lanche[-1])

print('Fatiamento com intervalo')

print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])  # do início até o elemento 2
print(lanche[-2:])  # começa da pizza e vai até o final

print('Tuplas são imutáveis')
# lanche[1] = 'Refrigerante'
print(lanche[1])
# print('TypeError: "tuple" object does not support item assignment')

print('Estrutura de repetição')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')  # vai mostrar lanche na posição cont

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))  # ordenado em ordem alfabética #lista

print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
c = b + a
print(c)
print(len(c))
print(c.count(5))  # quantas vezes 5 aparece na tupla c
print(c.index(2, 4))  # em que posição está o 2, a partir da posição 4

pessoa = ('Gustavo', 39, 'M', 99.88)  # aceita diferentes valores e tipos
print(pessoa)
# mas você não pode deletar um item da tupla
# del(pessoa[0])
# print(pessoa)
del pessoa  # apaga a tupla
print(pessoa)
