# Desenvolva um programa que leia o primeiro termo
# e a razão de uma P.A. No final, mostre os 10
# primeiros termos dessa progressão.


print(f'{" Desafio 051 ":=^30}')
n1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
print(f'Os 10 primeiros termos são: ')
decimo = n1 + (10 - 1) * r     # Fórmula da P.A
for i in range(n1, decimo + r, r):
    print(f'{i} ', end='')
