"""
Crie um programa que simule o funcionamento de um caixa
eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.

OBS --> Considere que o caixa possui cédulas de:
R$ 50
R$ 20
R$ 10
R$ 1
"""

print(f'{" Desafio 071 ":=^30}')


d = 'S'
while d == 'S':
    v = int(input('Digite o valor a ser sacado: '))

    v_50 = v_20 = v_10 = v_1 = 0  # variáveis são zeradas a cada valor inserido pelo cliente
    # caso contrário a cada valor as variáveis v_50, v_20, v_10, v_1 serão acumuladas com a entrada anterior

    while True:
        if v >= 50:
            v -= 50
            v_50 += 1
        elif v >= 20:
            v -= 20
            v_20 += 1
        elif v >= 10:
            v -= 10
            v_10 += 1
        elif v >= 1:
            v -= 1
            v_1 += 1
        else:
            break
    print(f'''
{v_50} notas de R$ 50
{v_20} notas de R$ 20
{v_10} notas de R$ 10
{v_1} notas de R$ 1
''')

    d = str(input('Deseja continuar[S/N]? ')).upper().strip()[0]

    if d != 'S':
        print('Programa encerrado!')
        break

