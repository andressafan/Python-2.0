'''Melhore o desafio 061, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos.'''

print(f'{" Desafio 061 ":=^30}')
print(f'{" Desafio 062 ":=^30}')

p = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
c = 9
print(f'{p}', end='')
while c != 0:
    c -= 1
    p += r
    print(', ', end='')
    print(f'{p}', end='')
    if c == 0:
        c = int(input('''
Deseja ver mais números?
Digite quantos quer ver, ou digite [0] para parar o programa: '''))
