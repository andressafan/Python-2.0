# Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem
# ou não formar um triângulo.

print(f'{"Desafio 034":=^30}')
c1 = float(input('Digite o comprimento do lado do triângulo: '))
c2 = float(input('Digite o comprimento do outro lado: '))
c3 = float(input('Digite o comprimento do outro lado: '))
if c1 - c2 < c3 < c1 + c2:
    print('É um triângulo')
elif c3 - c1 < c2 < c3 + c1:
    print('É um triângulo')
elif c3 - c2 < c1 < c3 + c2:
    print('É um triângulo')
else:
    print('Não é triângulo')
