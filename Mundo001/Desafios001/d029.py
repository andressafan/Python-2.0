# Escreva um programa que leia a velocidade
# de um carro.

# Se ele ultrapassar 80 km/h, mostre uma mensagem
# dizendo que ele foi multado.

# A multa vai custar
# R$ 7,00 por cada km acima do limite.

print(f'{"Desafio 029":=^30}')
v = int(input('Digite a velocidade: '))
m = 7 * (v - 80)
if v >= 80:
    print('O limite de velocidade é de 80 km/h')
    print(f'Você foi multado, por sua velocidade de {v} km/h')
    print(f'Sua multa será no valor de {m}')
else:
    print('Sua velocidade, está respeitando o limite estabelecido!')
