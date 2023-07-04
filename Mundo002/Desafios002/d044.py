# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de pagamento:

# — À vista dinheiro/cheque: 10% de desconto
# — À vista no cartão: 5% de desconto
# — Em até 2x no cartão: preço normal
# — 3x ou mais no cartão: 20% de juros
import math
print(f'{" Desafio 044 ":=^30}')
v = float(input('Digite o valor do produto: '))
c = str(input('''Digite um número para condição de pagamento
[1] - À vista dinheiro/cheque: 10% de desconto
[2] - À vista no cartão: 5% de desconto
[3] - Em até 2x no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros
: '''))
v_inicial = v
if c == '1':
    d = v * 0.1
    v -= (v * 0.1)
    print(f'Você teve um desconto de {d:.2f} R$ na sua compra!')
    print(f'Sua compra de {v_inicial:.2f} R$, ficará por {v:.2f} R$')
elif c == '2':
    d = v * 0.05
    v -= (v * 0.05)
    print(f'Você teve um desconto de {d:.2f} R$')
    print(f'Sua compra de {v_inicial:.2f} R$, ficará por {v:.2f} R$')
elif c == '3':
    p = v / 2
    print(f'Em duas parcelas de {p:.2f} R$')
    print(f'Sua compra de {v_inicial:.2f} R$, ficará por {v:.2f} R$')
elif c == '4':
    j = v + (v * 0.2)
    p = int(input('Digite o número de parcelas: '))
    parc = j / p
    print(f'Sua compra terá {p} parcelas de {parc:.2f} R$')
    print(f'E o valor de {v_inicial:.2f} R$, com um juros de {v * 0.2:.2f} R$, ficará por {j:.2f} R$')
else:
    print('Opção inválida de pagamento. Tente novamente!')
