# Desenvolva um programa que pergunte a distância
# de uma viagem em km. Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200 km
# e R$ 0,45 para viagens mais longas.

print(f'{"Desafio 031":=^30}')
d = int(input('Digite  a distância em km: '))
v1 = d * 0.5
v2 = d * 0.45
if d >= 200:
    print(f'A valor da sua passagem será de {v1}')
else:
    print(f'O valor da sua passagem é de {v2}')
