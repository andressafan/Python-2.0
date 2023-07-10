"""
Faça um programa que leia 5 valores numéricos e guarde-os
em uma lista

No final, mostre qual foi o maior e o menor valor digitado
e as suas respectivas posições na lista.
"""
print(f'{" Desafio 078 ":=^50}')
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

print('=' * 50)

print(f"""
lista: {lista}
maior: {maior}
menor: {menor}
""")

print('=' * 50)

for v in range(0, len(lista)):  # esse laço percorre o tamanho da lista
    # v == 0
    # começando do índice 0 até o último índice da lista (v)
    comp = lista[v]  # essa variável é um comparador ela recebe o elemento da lista no índice v
    # ex: lista = [1, 3, 5, 6, 7]
    # no primeiro laço comp = lista[0] --> comp == 1
    for i in range(v + 1, len(lista)):  # esse laço percorre o segundo índice da lista até o comprimento da lista
        # ex: no primeiro laço i == 1
        if comp == lista[i]:  # o primeiro elemento da lista vai ser comparado
            # com os elementos posteriores até o fim da lista
            # se eles forem iguais a menssagem a seguir será printada na tela
            print('Repetições: ')
            print(f'O valor {comp} aparece na posição {v + 1} e na posição {i + 1}')

