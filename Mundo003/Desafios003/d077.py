"""
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são suas vogais.
"""

print(f'{" Desafio 077 ":=^30}')

tupla = ('agua', 'arroz', 'feijao', 'cafe', 'pao', 'maça', 'carne'
         , 'bombom', 'suco')

for i in range(len(tupla)):
    print(f'A palavra {tupla[i]} tem as vogais:', end='')
    if 'a' in tupla[i]:
        print(f' a', end='')
    if 'e' in tupla[i]:
        print(f' e', end='')
    if 'i' in tupla[i]:
        print(f' i', end='')
    if 'o' in tupla[i]:
        print(f' o', end='')
    if 'u' in tupla[i]:
        print(f' u', end='')
    print('\n')


# Como o Guanabara fez:

for p in tupla:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')