"""
Crie um programa onde o usuário possa digitar 5 valores
numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""

lista = list()

for i in range(5):
    v = int(input('Digite um valor: '))
    lista.append(v)

for i in range(5):
    n = 0
    for v in lista:
        lista[n] = v = menor
        n += 1
        if v < menor:
            menor = v
    lista.insert(0, menor)

print(lista)

