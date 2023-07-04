# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.

print(f'{"Desafio 033":=^30}')
maior = 0
continuar = True
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n3 < n1 < n2 or n3 == n1 < n2:
    maior = n2
elif n1 < n2 < n3 or n1 == n2 < n3:
    maior = n3
elif n2 < n3 < n1 or n2 == n3 < n1:
    maior = n1
elif n1 == n2 == n3:
    maior = n1
    print('Todos são iguais')
    continuar = False
if continuar:
    print(f'O maior número é {maior}')

# Formato do Guanabara
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
