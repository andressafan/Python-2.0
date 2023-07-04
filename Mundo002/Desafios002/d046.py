# Faça um programa que mostre uma contagem regressiva
# na tela para o estouro de fogos de artifício, indo de 10
# até 0, com pause de 1 segundo entre eles.


from time import sleep

print(f'{" Desafio 046 ":=^30}')
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('Feliz ano novo!!!')
