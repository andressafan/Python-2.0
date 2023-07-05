"""Escreva um programa que leia um número n inteiro
qualquer e mostre na tela os n primeiros elementos de uma
Sequência de Fibonacci.

Ex:
  0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8"""
#           p1
print(f'{" Desafio 063 ":=^30}')

n = int(input('Digite quantos termos da sequência de Fibonacci deseja ver: '))
p1 = 0
p2 = 1
n -= 2

print(f'{p1} -> {p2}', end='')

while n != 0:
    print(' -> ', end='')
    n -= 1
    p1, p2 = p2, p1 + p2
    print(p2, end='')

print('.')
