# Faça um programa que leia a largura e a altura
# de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta,
# pinta uma área de 2m².

print('{:=^30}'.format('Desafio 011'))
larg = float(input('Digite a largura da sua parede em metros: '))
h = float(input('Digite a altura de sua parede em metros: '))
a = larg * h
q = a / 2
print('Para pintar a sua área de {}m²'.format(a))
print('Você precisará de {}L de tinta'.format(q))
