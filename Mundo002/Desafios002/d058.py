"""Melhore o jogo do Desafio 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar, mostrando no final quantos palpites foram necessários
para vencer."""

import random
import time


print(f'{" Desafio 028 ":=^30}')
print(f'{" Desafio 058 ":=^30}')

print(f'{" Jogo de Adivinhação ":=^30}')
n = int(input('Pense em um número de 0 a 10: '))
c = random.randint(0, 10)
x = 0
while n != c:
    print('O computador está pensando...')
    time.sleep(1)
    print(f'Você errou! o computador escolheu {c} e você escolheu {n}')
    c = random.randint(0, 10)
    n = int(input('Faça uma nova tentativa, digite outro número: '))
    x += 1
print('O computador está pensando...')
time.sleep(1)
print(f'Acertou!!! o computador escolheu {c} e você também escolheu {n}')
print(f'Você teve {x} tentativas!')
