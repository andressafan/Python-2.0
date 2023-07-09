"""
Faça um programa que leia 5 valores numéricos e guarde-os
em uma lista

No final, mostre qual foi o maior e o menor valor digitado
e as suas respectivas posições na lista.
"""

lista = list()
maior = menor = 0
for i in range(5):
    lista.append(int(input('Digite um valor: ')))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    if lista[i] > maior:
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]

for valor in range(5):  # somente uma iteração valor == [0]
    for pos, ele in enumerate(lista):  # passa por cada elemento da lista
        if lista[valor] == ele:
            print(f'O valor {lista[valor]} aparece na posição {pos}')


print(f'''
lista: {lista}
maior: {maior}
menor: {menor}''')
