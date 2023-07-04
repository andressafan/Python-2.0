# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando uma mensagem na tela:

# — O primeiro valor é o maior
# — O segundo valor é o maior
# — Não existe valor maior, os dois são iguais

print(f'{"Desafio 038":=^30}')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O número {n1} é o maior')
elif n2 > n1:
    print(f'O número {n2} é o maior')
else:
    print('Não existe valor maior, os dois são iguais')
