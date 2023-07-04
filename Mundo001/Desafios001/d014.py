# Faça um programa que converta temperaturas digitadas
# em C° para F°.

print('{:=^30}'.format('Desafio 014'))
t = float(input('Digite a temperatura em Celsius: '))
f = (t * 1.8) + 32
print('A temperatura de {}°C corresponde a {}°F'.format(t, f))
