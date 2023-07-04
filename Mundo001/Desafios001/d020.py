# O mesmo professor do desafio anterior quer sortear
# a ordem de apresentação de trabalhos dos alunos. Faça um
# programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

"""import random
print(f'{"Desafio 020":=^30}')
a1 = str(input('Digite o nome de um aluno: '))
a2 = str(input('Digite o nome de outro aluno: '))
a3 = str(input('Digite o nome de outro aluno: '))
a4 = str(input('Digite o nome de outro aluno: '))
l = [a1, a2, a3, a4]
print('A sequência sorteada foi: {}'.format(random.choice(l)))"""

# Não resolvido
# Resolução Guanabara:

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
# shuffle : embaralhar
print('A ordem de apresentação será:')
print(lista)
