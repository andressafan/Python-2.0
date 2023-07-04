# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

print(f'{" Desafio 056 ":=^30}')
tidade = 0  # acumulador
hmaior = 0  # acumulador
fcont = 0  # contador
for i in range (4):
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    tidade += idade
    if sexo == 'M':
        if idade > hmaior:
            hmaior = idade
            nmaior = nome
    if sexo == 'F':
        if idade < 20:
            fcont += 1
m = tidade / 4
print(f'A média de idade do grupo é de {m} anos')
print(f'O homem mais velho tem {hmaior} anos e se chama {nmaior}.')
print(f'Ao todo são {fcont} mulheres com menos de 20 anos')
