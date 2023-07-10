"""
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma descrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = list()


while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    d = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if d != 'S':
        print('Programa Encerrado!')
        break

lista.sort(reverse=True)

print(f'''
Quantidade de números: {len(lista)}
Lista em ordem decrescente: {lista}
5 está na lista?  {'Sim' if 5 in lista else 'Não'}
''')
