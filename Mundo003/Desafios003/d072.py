"""
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
"""
print(f'{" Desafio 072 ":=^30}')

n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartorze',
     'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        num = int(input('Valor Inválido! Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {n[num]}')
    d = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if d != 'S':
        print('Programa encerrado!')
        break
