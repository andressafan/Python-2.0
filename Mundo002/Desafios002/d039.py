# Faça um programa que leia o ano de nascimento de um jovem
# e informe, conforme a sua idade:

# — Se ele ainda vai se alistar ao serviço militar
# — Se é a hora de se alistar
# — Se já passou do tempo do alistamento

# O seu programa também deverá mostrar o tempo que
# falta ou que passou do prazo.

from datetime import date
print(f'{"Desafio 039":=^30}')
a = int(input('Informe seu ano de nascimento: '))
ano_atual = date.today().year
i = ano_atual - a
f = 18 - i
p = i - 18
if i == 18:
    print(f'Você tem {i} anos, e deve fazer o alistamento militar')
elif i < 18:
    print(f'Você tem {i} anos, e faltam {f} ano(s) para se alistar')
    print(f'O ano do alistamento será em {ano_atual + f}')
elif i > 18:
    print(f'Você tem {i} anos, e já se passaram {p} ano(s) do período de alistamento')
    print(f'O ano do alistamento foi em {ano_atual - p}')
