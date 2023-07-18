"""
Aprimore o desafio 093 para que ele funcione com vários jogadores
, incluindo um sistema de visualização de detalhes de aproveitamento
de cada jogador.
cod nome gols total
levantamento por cod
"""

print(f'{" Desafio 095 ":=^50}')
time = list()

while True:
    jogador = dict()
    jogador['cod'] = len(time)
    jogador['Nome'] = str(input('Digite seu nome: '))
    p = int(input(f'Digite o número de partidas que {jogador["Nome"]} jogou: '))

    gols = []
    for i in range(p):
        gols.append(int(input(f'Digite quantos gols fez na partida {i+1}: ')))

    jogador['Gols'] = gols
    jogador['Total'] = sum(gols)
    time.append(jogador)

    d = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if d != 'S':
        print('Encerrando...')
        break

print('='*50)
print(f'{"Cod":<3}{"Nome":<15}{"Gols":<15}{"Total":<15}')
print('='*50)
for jogador in time:
    print(f'{jogador["cod"]:<3}{jogador["Nome"]:<15}{str(jogador["Gols"]):<15}{jogador["Total"]:<15}')
print('='*50)

while True:
    cod = int(input('Digite o código do jogador para ver os detalhes (999 para sair): '))
    if cod == 999:
        print('Encerrando...')
        break

    if cod >= len(time):
        print('Código inválido. Tente novamente.')
    else:
        jogador = time[cod]
        print(f'\nLevantamento do jogador {jogador["Nome"]}:')
        for i, gols in enumerate(jogador['Gols']):
            print(f'Na partida {i+1} fez {gols} gols.')
        print(f'Total de gols: {jogador["Total"]}')
        print('='*50)
