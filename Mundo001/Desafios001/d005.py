# Faça um programa que leia um número inteiro e mostre na tela
# o seu sucessor e o seu antecessor.

print('{:=^30}'.format('Desafio 006'))
n = int(input('Digite um número inteiro: '))
print('Analizando o número {}'.format(n))
print('O antecessor é: {}\ne o sucessor: {}'.format(n - 1, n + 1))
