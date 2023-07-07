"""
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos preços,
na sequência.

No final, mostre uma listagem de preços, organizando os dados
em forma tabular.

Lápis ---------- R$ 1.75
Caneta --------- RS 0.50
"""

print(f'{" Desafio 076 ":=^35}')
tupla = ('Lápis', 1.75, 'Caneta', 2.00, 'Estojo', 25.00, 'Caderno'
         , 30.00, 'Borracha', 0.50, 'Grafite', 0.75, 'Resma Folha A4', 20.00
         , 'Régua', 5.00)
print(f'{" Tabela de Preços ":=^35}')

for i in range(0, len(tupla), 2):  # percorre do índice 0 até o fim da tuplas, pulando de 2 em dois
    nome = tupla[i]
    preco = tupla[i+1]
    print(f"{f'{nome:-<15}' + '-' * 10 + f'R$ {preco:<4.2f}':^35}")
