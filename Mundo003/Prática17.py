"""num = (2, 5, 9, 1)  # ---> tupla
num[2] = 3
print(num)  # --> erro tuplas são imutáveis!"""

num = [2, 5, 9, 1]  # --> lista
print(f'Lista:\n{num}')
num[2] = 3
print(f'Lista após colocar o número 3 na posição [2]:\n{num}')
num.append(7)
print(f'Lista após adicionar o elemento 7:\n{num}')
num.sort()
print(f'Lista após ordenar com a função sort:\n{num}')
num.sort(reverse=True)
print(f'Lista após ordenar em ordem decrescente:\n{num}')
num.insert(2, 0)
print(f'Lista após adicionar o elemento 0 na posição [2]:\n{num}')
num.pop()
print(f'Lista após eliminar o último elemento:\n{num}')
print(f'Essa lista tem {len(num)} elementos')

print('-' * 45)

lista = [7, 3, 5, 3, 8]
print(f'Lista:\n{lista}')
lista.remove(3)
print(f'Lista após remover o elemento 3:\n{lista}')
print('Note que só é removida a primeira ocorrência do 3')

print('-' * 45)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for c, v in enumerate(valores):
    print(f'{v} na posição {c}')
