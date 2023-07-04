# Escreva um programa que faça o computador
# 'pensar' num número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o
# escolhido pelo computador

# O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

import time
import random

print(f'{"Desafio 028":=^30}')
num = int(input('Escolha um número de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
esc = random.choice(lista)
print(f'O número que você escolheu foi {num}')
print('Processando...')
time.sleep(3)
print(f'O número sorteado foi: {esc}')
if esc == num:
    print('Parabéns você acertou!!!!')
else:
    print('Não foi dessa vez, tente de novo!')
