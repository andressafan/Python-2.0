"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo e realize
a contagem.

Seu programa tem que realizar três contagens através da função
criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.

"""
print(f'{" Desafio 098 ":=^50}')


def contador(inicio, fim, passo):
    if passo == 0:
        print("Erro: O passo não pode ser igual a zero.")
        return

    if inicio > fim and passo > 0:
        passo = -passo

    if inicio < fim and passo < 0:
        passo = -passo

    if inicio <= fim:
        contagem = range(inicio, fim + 1, passo)
    else:
        contagem = range(inicio, fim - 1, passo)

    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}:")
    for i in contagem:
        print(f'{i},', end=' ')
    print("FIM")


# Contagem de 1 até 10, de 1 em 1
contador(1, 10, 1)

# Contagem de 10 até 0, de 2 em 2
contador(10, 0, 2)

# Contagem personalizada
inicio = int(input('Digite o número para início da contagem: '))
fim = int(input('Digite o número para fim da contagem: '))
passo = int(input('Digite o passo para contagem: '))
contador(inicio, fim, passo)

