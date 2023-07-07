"""
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final mostre:

A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares.
"""

print(f'{" Desafio 075 ":=^30}')

n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite outro número: ')),
     int(input('Digite outro número: ')))
print(f'Você digitou os valores {n}')
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3) + 1}')
else:
    print(f'O número 3 não aparece em nenhuma posição!')
print(f'Os números pares são: ', end='')
for i in n:
    if i % 2 == 0:
        print(f'{i}, ', end='')
