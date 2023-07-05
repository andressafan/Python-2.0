"""Faça um programa que leia um número qualquer e mostre
o seu fatorial.
ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

print(f'{" Desafio 060 ":=^30}')

n = int(input('Digite um número: '))  # 5
c = n  # contador = 5 # 4 # 3 # 2 # 1
v = n  # 5 # 4 # 3 # 2 # 1
fat = v  # 5 # 20 # 60 # 120 # 120
print(f'{n}! = {v}', end='')  # 5! = 5
while c != 1:  # enquanto c for diferente de 1 o programa continua
    c -= 1  # 4 # 3 # 2 # 1 # parada
    v -= 1  # 4 # 3 # 2 # 1
    fat *= v  # 5 * 4 = 20 # 20 * 3 # 60 * 2 # 120 * 1
    print(f' x {v}', end='')  # x 4 # x 3# x 2# x 1
print(f' = {fat}')  # = 120
