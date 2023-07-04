# A confederação nacional de natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre a sua categoria,
# conforme a idade:

# — Até 9 anos: MIRIM
# — Até 14 anos: INFANTIL
# — Até 19 anos: JUNIOR
# — Até 25 anos: SÊNIOR
# — Acima: MASTER

from datetime import date
print(f'{"Desafio 041":=^30}')
a = int(input('Digite seu ano de nascimento: '))
a_atual = date.today().year
i = a_atual - a
print(f'O atleta tem {i} anos')
if i <= 9:
    print('MIRIM')
elif i <= 14:
    print('INFANTIL')
elif i <= 19:
    print('JUNIOR')
elif i <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
