"""
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado. No final, serão exibidos
todos os valores únicos digitados, em ordem crescente.

"""
lista = list()

while True:
    d = int(input('Digite um valor:'))
    if d not in lista:
        lista.append(d)
    e = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if e != 'S':
        break
print(f'Sua lista: {lista}')
lista.sort()
print(f'Sua lista em ordem crescente: {lista}')
