# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já sõa maiores.


from datetime import date
print(f'{" Desafio 053 ":=^30}')
contmm = 0
contm = 0
for i in range(7):
    nasc = int(input('Digite seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = ano_atual - nasc
    if idade < 18:
        print(f'Você tem {idade} anos')
        print('Você ainda não atingiu a maioridade!')
        contmm += 1
    elif idade >= 18:
        print(f'Você tem {idade} anos')
        print('Você já atingiu a maioridade!')
        contm += 1
print(f'{contmm} pessoas ainda não atingiram a maioridade!')
print(f'{contm} pessoas já atingiram a maioridade!')

