# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
# Divisível por um e por ele mesmo

'''print(f'{" Desafio 052 ":=^30}')
num = int(input('Digite um número: '))
for i in range(1, num+1):
    if num % i == 0:
        print(f'{num} é um número primo')
    else:
        print(f'{num} não é primo')
'''

print(f'{" Desafio 052 ":=^30}')
num = int(input('Digite um número: '))
s = 0  # contador
p = 0  # acumulador
for i in range(1, num+1):
    if num % i == 0:
        s += 1
        p += i
if p == num + 1:
    print('é primo')
else:
    print('não é primo')

# jeito do guanabara

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
