# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daquelas que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

print(f'{" Desafio 050 ":=^30}')
s = 0
for i in range(0, 7, 2):
    s += i
print(f'A soma dos números é igual a {s}')

s = 0
c = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}° valor: '))
    if num % 2 == 0:
        c += 1
        s += i
print(f'Você digitou {c} números pares e a soma dos números é igual a {s}')
