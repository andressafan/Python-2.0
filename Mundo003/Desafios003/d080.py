"""
Crie um programa onde o usuário possa digitar 5 valores
numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.
"""
print(f'{" Desafio 080 ":=^50}')
lista = list()

menor = 0
maior = 0
for i in range(5):
    v = int(input('Digite um valor: '))
    if i == 0:
        menor = v
        maior = v
        lista.append(v)
    if v < menor:
        menor = v
        lista.insert(0, v)
    if v > maior:
        maior = v
        lista.append(v)
    if menor < v < maior:
        lista.insert(1, v)

print(f'Em ordem crescente: {lista}')
print('=' * 50)
print('Como o Guanabara resolveu: ')

listag = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        listag.append(n)
    elif n > listag[len(listag)-1]:  # se o número for maior q o número que está no último elemento ou (lista[-1])
        listag.append(n)
    else:
        pos = 0
        while pos < len(listag):
            if n <= listag[pos]:
                listag.insert(pos, n)
                break
            pos += 1
print('=' * 50)
print(f'Os valores digitados em ordem foram {listag}')
