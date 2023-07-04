nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
# Dessa forma faz com que a variável nome
# apareça em 20 caracteres.
# Gustavo_____________!
print('Prazer em te conhecer {:<20}!'.format(nome))
# (<) Alinhado à esquerda
# _____________Gustavo!
print('Prazer em te conhecer {:^20}'.format(nome))
# (^) Centralizado
# _______Paulo_______!
print('Prazer em te conhecer {:=^20}!'.format(nome))
# (=) Centralizado em vinte espaços entre (=)
# ========Ana=========!
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1+n2))
# ou
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} \nO produto {} \nA divisão é {:.3f}'.format(s, m, d), end='')
# Formatação {:.3f}
# Depois da vírgula terá três casas decimais {3 pontos (f)lutuantes}
# 1.333333333 ---> 1.333
# (, end='') formatação do print com métodos
# (, end=' >>>> ')...
# usando o método acima o print cola no seguinte, sem a separação de linha
# \n ---> (nova linha) (quebra de linha)
print('\nDivisão inteira {} e potência {}'.format(di, e))
