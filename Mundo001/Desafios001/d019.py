# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.
import random
from random import randrange

import random

print(f'{"Desafio 019":=^30}')
a1 = str(input('Digite o primeiro nome: '))
a2 = str(input('Digite o segundo nome: '))
a3 = str(input('Digite o terceiro nome: '))
a4 = str(input('Digite o quarto nome: '))
lista = [a1, a2, a3, a4]
print('O aluno sorteado foi o {}'.format((random.choice(lista))))
