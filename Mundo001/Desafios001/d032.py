# Faça um programa que leia um ano qualquer
# e mostre se ele é bissexto.


print(f'{"Desafio 032":=^30}')
ano = int(input('Digite o ano para analisar: '))
if ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print('Não é bissexto!')
