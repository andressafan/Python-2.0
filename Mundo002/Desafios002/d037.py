# Escreva um programa que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão:
# — 1 para binário
# — 2 para octal
# — 3 para hexadecimal


print(f'{"Desafio 037":=^30}')
n = int(input('Digite um número: '))
c = int(input('''Digite um número para escolher a base de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal
: '''))
if c == 1:
    # Fatiamento: [2:] começa no segundo índice e vai até o final
    print(f'{n} convertido para binário é igual a {bin(n)[2:]}')
elif c == 2:
    print(f'{n} convertido para octal é igual a {oct(n)[2:]}')
elif c == 3:
    print(f'{n} convertido para hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção inválida!')
