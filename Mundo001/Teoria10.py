# Condições Simples e Compostas

# Estrutura sequêncial
# carro.siga() #todo método tem parênteses no final
# carro.esquerda()
# carro.siga()
# carro.direita()
# carro.siga()
# carro.direita()
# carro.siga()
# carro.esquerda()
# carro.siga()

# Possibilidades
# Estrutura condicional
#                   carro.siga()
#  se carro.esquerda()            senão

#  carro.direita()               carro.esquerda()
#  carro.siga()                  carro.siga()
#  carro.direita()               carro.esquerda()
#  carro.esquerda()              carro.siga()
#  carro.siga()
#  carro.direita()
#  carro.siga()
#                   carro.para()

#                e identado fica assim:
#  carro.siga()
#  se carro.esquerda()
#       carro.siga()
#       carro.direita()
#       carro.siga()
#       carro.direita()
#       carro.esquerda()
#       carro.siga()
#       carro.direita()
#       carro.siga()
#  senão
#       carro.siga()
#       carro.esquerda()
#       carro.siga()
#       carro.esquerda()
#       carro.siga()
#  carro.pare()

#         Em Python:

#  if carro.esquerda():
#       bloco True
#  else:
#       bloco False

# tempo = int(input('Quantos anos tem o seu carro?'))
# if tempo <= 3:
#   print('carro novo')
# else:
#   print('carro velho')
# print('Fim')
