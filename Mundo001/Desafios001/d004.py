# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

n = input('Digite algo: ')
print(type(n))
print(n.isalpha())
# testa se é caractere
print(n.isnumeric())
# testa se é número
print(n.istitle())
# testa se está no formato title (com a primeira letra em caixa alta)
print(n.islower())
# testa se todas as letras estão minúsculas (para isso deve se tratar de carcteres e não números)
print(n.isalnum())
# testa se é alfanumérico (número ou letra)
print(n.isprintable())
# testa se é imprimível na tela (não faz sentido)
print(n.isdecimal())
# testa se é um número decimal
print(n.isupper())
# testa se a palavra está toda em caixa alta
print(n.isascii())
# testa se são carcteres ascii
print(n.isspace())
# testa é espaço
print(n.isidentifier())



