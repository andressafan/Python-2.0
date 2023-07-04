# Faça um programa que leia um número
# de 0 a 9999 e mostre na tela cada um dos
# digitos separados.

"""print(f'{"Desafio 023":=^30}')
num = str(input('Digite um número de 0 a 9999: ')).strip().replace('.', '')
print(num)
print(f'Unidade: {num[3]}')
print(f'Dezena: {num[2]}')
print(f'Centena: {num[1]}')
print(f'Milhar: {num[0]}')
"""

# Matematicamente...

'''print(f'{"Desafio 023":=^30}')
num = int(input('Digite um número 0 a 9999: '))
#  pega o ultimo número
unit = num%10
#  remove o ultimo e salva
num = num//10
#  mostra
print(f'{unit} unidades')
deze = num%10
num = num //10
print(f'{deze} dezenas')
cent = num%10
num = num //10
print(f'{cent} centenas')
milhar = num
print(f'{num} milhares')'''

num = int(input('Digite um número 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidades: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Milhar: {m}')
