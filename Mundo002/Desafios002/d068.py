"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo
"""

print(f'{" Desafio 068 ":=^30}')

print(f'{" Par ou Ímpar ":=^30}')

import random


v = s = 0

while True:
    e = str(input('Você escolhe ímpar ou par [I/P]? ')).strip().upper()[0]
    j = int(input('Escolha um número de 0 a 10: '))
    c = random.randint(0, 10)
    s = j + c
    if s % 2 == 0 and e == 'P':
        print(f'O computador escolheu {c} e você {j}')
        print('Você acertou!!')
        v += 1
    elif s % 2 != 0 and e == 'I':
        print(f'O computador escolheu {c} e você {j}')
        print('Você acertou!!')
        v += 1
    else:
        print(f'O computador escolheu {c} e você {j}')
        print('Você errou!')
        break
print(f'Você teve {v} vitórias consecutivas!')


