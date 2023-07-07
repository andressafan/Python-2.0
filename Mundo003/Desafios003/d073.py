"""
Crie uma tupla preenchida com os 20 primeiros colocados da tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela esta o time da Chapecoense
"""

c = ('Vila Nova', 'Sport Recife', 'Criciúma', 'Novorizontino', 'EC Vitória',
     'Mirassol', 'Juventude', 'Botafogo SP', 'Guarani', 'Atlético-GO',
     'CRB', 'Ceará SC', 'Ituano', 'Ponte Preta', 'Sampaio Corrêa',
     'Tombense', 'Chapecoense', 'Londrina', 'Avaí', 'ABC')

print(f'{" Desafio 073 ":=^30}')
print(f'{" 5 primeiros colocados ":=^30}')
for pos, c in enumerate(c):
    if pos < 5:
        print(f'{c}' + f'{"." * 10}' + f'{pos + 1}° lugar')
    else:
        break

c = ('Vila Nova', 'Sport Recife', 'Criciúma', 'Novorizontino', 'EC Vitória',
     'Mirassol', 'Juventude', 'Botafogo SP', 'Guarani', 'Atlético-GO',
     'CRB', 'Ceará SC', 'Ituano', 'Ponte Preta', 'Sampaio Corrêa',
     'Tombense', 'Chapecoense', 'Londrina', 'Avaí', 'ABC')

print(f'{" 4 últimos colocados ":=^30}')
for cont in range(len(c) - 4, len(c)):  # começa no elemento - 4 e vai ate o comprimento da tupla
    print(f'{c[cont]}' + f'{"" :.^10}' + f'{cont + 1}° lugar')

print(f'{" Ordenado Afabeticamente ":=^30}')
c = sorted(c)
for i in range(0, len(c)):
    print(c[i])

c = ('Vila Nova', 'Sport Recife', 'Criciúma', 'Novorizontino', 'EC Vitória',
     'Mirassol', 'Juventude', 'Botafogo SP', 'Guarani', 'Atlético-GO',
     'CRB', 'Ceará SC', 'Ituano', 'Ponte Preta', 'Sampaio Corrêa',
     'Tombense', 'Chapecoense', 'Londrina', 'Avaí', 'ABC')

print(f'{" Posição da Chapecoense ":=^30}')

for i in range(0, len(c)):
    if c[i] == 'Chapecoense':
        print(f'Chapecoense está na posição: {i + 1}')

# Como o Guanabara fez:


print(f'{" Resolução do Guanabara ":*^30}')


times = ('Vila Nova', 'Sport Recife', 'Criciúma', 'Novorizontino', 'EC Vitória',
         'Mirassol', 'Juventude', 'Botafogo SP', 'Guarani', 'Atlético-GO',
         'CRB', 'Ceará SC', 'Ituano', 'Ponte Preta', 'Sampaio Corrêa',
         'Tombense', 'Chapecoense', 'Londrina', 'Avaí', 'ABC')


print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'O 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}° posição')
