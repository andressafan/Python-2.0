'''Crie um programa que leia vários números inteiros
pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando a flag)'''

print(f'{" Desafio 064 ":=^30}')
n = int(input('Digite um número ou digite "999" para parar: '))
c = 1
soma = n
while n != 999:
    n = int(input('Digite outro número ou "999" para parar: '))
    if n != 999:
        c += 1
        soma += n
print(f'Você digitou {c} números e a soma entre eles é: {soma}')