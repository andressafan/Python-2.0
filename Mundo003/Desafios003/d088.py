"""
Faça um programa que ajude um jogador da Mega Sena a criar
palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrado
tudo em uma lista composta.
"""
from random import randint
from time import sleep
lista = list()
print(f'{" Desafio 088 ":=^50}')
print(f'{" M E G A  S E N A ":=^50}')
q = int(input('Quantos jogos você quer sortear? '))
for i in range(q):
    for num in range(6):
        numero = (randint(1, 60))
        if num not in lista:
            lista.append(numero)
    lista.sort()
    sleep(1)
    print(f'Jogo {i + 1}: {lista}')
    lista.clear()
