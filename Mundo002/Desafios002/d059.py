'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

print(f'{" Desafio 059 ":=^30}')

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
e = 0
while e != 5:
    e = int(input('''Escolha uma opção do menu:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    '''))
    if e == 1:
        x = n1 + n2
        print(f'Soma: {x}')
    elif e == 2:
        x = n1 * n2
        print(f'Multiplicação: {x}')
    elif e == 3:
        if n1 < n2:
            print(f'Maior: {n2}')
        if n2 < n1:
            print(f'Maior: {n1}')
        elif n1 == n2:
            print('São o mesmo valor!')
    elif e == 4:
        print('Deseja mudar os números? Insira-os a seguir:')
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
print('Você saiu do programa!')
