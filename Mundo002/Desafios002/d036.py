# Escreva um programa para aprovar um empréstimo
# bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salário ou então o empréstimo será negado.

print(f'{"Desafio 036":=^30}')
# Replace vai tirar o ponto caso o usuário coloque para não dar erro
v = str(input('Digite o valor da casa: ')).replace('.', '').replace(',', '')
comprador = str(input('Digite seu salário: ')).replace('.', '').replace(',', '')
c = float(comprador)
valor = float(v)
a = int(input('Em quantos anos pretente pagar? '))
m = a * 12
p_a = valor / a
p = valor / (12 * a)
if p > c + (c * 0.3):
    print('Empréstimo negado!')
else:
    print(f'O valor da prestação da casa ficará por {p:.2f} R$ ao mês, em {a} anos')
    print(f'Totalizando {p_a:.2f} R$ por ano')

