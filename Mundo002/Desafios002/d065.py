'''Crie um programa que leia vários números inteiros
pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valor lido. O programa
deve perguntar ao usuário se ele quer ou não continuar a digitar valores'''


n = int(input('Digite um número: '))
p = 'S'
soma = n
c = 1
maior = menor = n

while p != 'N':
    n = int(input('Digite outro número: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    p = str(input('''
Deseja adicionar mais números?
Se sim digite qualquer letra, se não digite "N": ''')).upper()
    soma += n
    c += 1

media = soma/c
print(f'''
Você adicionou {c} números
Média: {media}
Maior: {maior}
Menor: {menor}''')

