# Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo desconsiderando os espaços.

# Ex: APOS A SOPA

"""print(f'{" Desafio 053 ":=^30}')
frase = input('Digite sua frase: ').split()
for i in range(,-1):
    print(frase)"""

"""print(f'{" Desafio 053 ":=^30}')
frase = str(input('Digite sua frase: ')).strip()
frase = frase[0:]
for i in range(0, frase+1, -1):
    print(i)"""

# não sei

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

# outra forma

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
