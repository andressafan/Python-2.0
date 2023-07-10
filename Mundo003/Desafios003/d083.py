"""
Crie um programa onde o usuário digite uma expressão
qualquer que use parêntese. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados
na ordem correta.
"""

e = str(input('Digite uma expressão algébrica (com parênteses): '))

while True:
    for pos, i in enumerate(e):
        if '(' in e:
            inicio = pos
            if ')' not in pos > inicio:
                print('não valido')
