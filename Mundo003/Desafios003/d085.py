"""

Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre
os valores pares e ímpares em ordem crescente

"""


print(f'{" Desafio 085 ":=^50}')

lista = [[], []]
for i in range(5):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 != 0:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(lista)
