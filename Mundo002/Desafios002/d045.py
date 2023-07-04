# Crie um programa que faça o computador jogar Jokenpô com você
import random
import time
print(f'{" Desafio 045 ":=^30}')
print(f'{" Jokenpô ":*^30}')
esc = str(input('''Digite sua escolha
- Pedra
- Papel
- Tesoura
: ''')).capitalize()
lista = ['Pedra', 'Papel', 'Tesoura']
comp = random.choice(lista)
print('Processando...')
time.sleep(3)
if comp == esc:
    print('Empate!')
    print(f'Você e o computador escolheram {comp}')
elif comp == 'Pedra' and esc == 'Papel':
    print(f'O computador escolheu {comp} e você {esc}')
    print('Você ganhou!')
elif esc == 'Pedra' and comp == 'Papel':
    print(f'O computador escolheu {comp} e você {esc}')
    print('Você Perdeu!')
elif comp == 'Tesoura' and esc == 'Papel':
    print(f'O computador escolheu {comp} e você {esc}')
    print('Você Perdeu!')
elif esc == 'Tesoura' and comp == 'Papel':
    print(f'O computador escolheu {comp} e você {esc}')
    print('Você Ganhou!')
elif comp == 'Pedra' and esc == 'Tesoura':
    print(f'O computador escolheu {comp} e você {esc}')
    print('Você Perdeu!')
elif esc == 'Pedra' and comp == 'Tesoura':
    print(f'O computador escolheu {comp} e você {esc}')
    print('Você Ganhou!')
else:
    print('Opção inválida, tente novamente!')

# Também poderia fazer assim:

itens = ('Pedra', 'Papel', 'Tesoura')  # tupla
computador = random.randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print(f'O computador escolheu {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
if computador == 0:  # computador jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')
    else:
        print('jogada inválida!')
elif computador == 1:  # computador jogou papel
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('jogador vence')
    else:
        print('jogada inválida!')
elif computador == 2:  # computador jogou tesoura
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('jogada inválida!')