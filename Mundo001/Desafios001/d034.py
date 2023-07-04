# EScreva um programa que pergunte o salário
# de um funcionário e calcule o valor do seu aumento

# --> Para salários superiores a R$ 1.250,00,
# calcule um aumento de 10%

# --> Para os inferiores ou iguais, o aumento é de 15%

print(f'{"Desafio 034":=^30}')
sal = float(input('Digite seu salário: '))
sup = sal + (sal * 0.1)
sub = sal + (sal * 0.15)
if sal > 1.250:
    print(f'''Seu salário de {sal},
reberá uma bonificação de {(sal * 0.1)},
totalizando {sup}''')
elif sal <= 1.250:
    print(f'''Seu salário de {sal},
receberá uma bonificação de {(sal * 0.15)},
totalizando {sub}''')
