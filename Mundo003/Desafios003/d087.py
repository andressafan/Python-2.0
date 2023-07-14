"""
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna
C) O maior valor da segunda coluna
"""

print(f'{" Desafio 087 ":=^50}')

matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        matriz[linha].insert(coluna, int(input(f'Digite um número para a posição {[linha, coluna]}: ')))

print('='*50)

s_p = s_ter = maior = 0
for lin in range(3):
    print()
    for col in range(3):
        print(f'[{matriz[lin][col]:^3}]', end='')
        if lin == 0 and col == 0:
            maior = matriz[lin][col]
        if matriz[lin][col] % 2 == 0:
            s_p += matriz[lin][col]
        if col == 2:
            s_ter += matriz[lin][col]
        if matriz[lin][col] > maior:
            maior = matriz[lin][col]
print()
print()

print('='*50)

print(f'''
A soma dos valores pares: {s_p}
A soma da terceira coluna: {s_ter}
O maior valor é: {maior}''')
