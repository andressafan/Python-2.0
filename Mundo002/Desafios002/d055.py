# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

'''print(f'{" Desafio 055 ":=^30}')
maior = menor = 0
for i in range(5):
    p = float(input('Digite seu peso: '))
    if p > maior:
        maior = p
    elif p < menor:
        menor = p
print(menor, maior)'''


print(f'{" Desafio 055 ":=^30}')
maior = menor = 0
for p in range(5):
    peso = float(input('Digite seu peso: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(menor, maior)
