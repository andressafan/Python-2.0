# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros

print('{:=^30}'.format('Desafio 008'))
print('{:-^30}'.format('Coversor de medidas'))
v = float(input('Digite um valor em metros: '))
km = v / 1000
hm = v / 100
dam = v / 10
dm = v * 10
c = v * 100
m = v * 1000

print('Em quilômetros: {:.2f}km\nEm hectômetros: {:.2f}hm\nEm decâmetros: {:.2f}dam'.format(km, hm, dam))
print('Em decímetros: {:.2f}dm\nEm centímetros: {:.2f} cm\nEm milímetros: {:.2f} mm'.format(dm, c, m))


