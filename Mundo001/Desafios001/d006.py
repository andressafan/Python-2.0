# Crie um algoritmo que leia um número e mostre
# o seu dobro, triplo e raiz quadrada.

print('{:=^30}'.format('Desafio 006'))
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print('O dobro vale: {}\nO triplo vale: {}\nA raiz quadrada vale: {:.2f}'.format(d, t, r))

# Evite criar muitas variáveis se possível: elas ocupam muito espaço na memória!
# pow(n, (1/2))
# função que calcula raiz quadrada
