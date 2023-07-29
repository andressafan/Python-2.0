"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável.
Ex: escreva('Olá, Mundo!')
Saída:
---------------
  Olá, Mundo!
---------------
"""

print(f'{" Desafio 097 ":=^50}')


def escreva(txt):
    tam = len(txt) + 10
    linha_sup = '=' * tam
    txt_cent = f'{txt:^{tam}}'
    print(linha_sup)
    print(txt_cent)
    print(linha_sup)


msg = input('Digite um texto: ')
escreva(msg)
