"""
Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteio() e somaPar(). A primeira
função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores
PARES sorteados pela função anterior.
"""

print(f'{"🎊 Desafio 100 🎊":=^50}')
lista = list()


def sorteio():
    from random import randint
    for i in range(5):
        n = randint(0, 100)
        lista.append(n)


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Sua lista gerada é {lista}')
    print(f'A soma dos números PARES é = {soma}')


sorteio()
somaPar(lista)
