"""Refaça o desafio 051, lendo o primeiro termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while."""

print(f'{" Desafio 061 ":=^30}')

p = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
c = 0
print(f'{p}', end='')
while c != 9:
    c += 1
    p += r
    print(f', {p}', end='')
