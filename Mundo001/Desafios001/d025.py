# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem 'SILVA' no nome.

print(f'{"Desafio 025":=^30}')
nome = input('Digite seu nome: ').upper()
if 'SILVA' in nome:
    print('Têm Silva no seu nome!')
else:
    print('Não tem Silva em seu nome!')
