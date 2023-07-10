"""
Crie um programa que vai ler vários números e colocar
em uma lista.

Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados,
respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""

lista = list()
lista_pares = list()
lista_impares = list()
while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    if v % 2 == 0:
        lista_pares.append(v)
    if v % 2 != 0:
        lista_impares.append(v)
    e = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if e != 'S':
        print('Programa encerrado!')
        break

print(f'''
Sua lista: {lista}
Sua lista somente com pares: {lista_pares}
Sua lista somente com ímpares: {lista_impares}
''')