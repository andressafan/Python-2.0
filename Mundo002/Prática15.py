# Prática

cont = 1
while cont <= 10:
    print(cont)
    cont += 1
print('Acabou')

cont = 1
while True:  # infinito
    print(cont)
    cont += 1
print('Acabou')

n = s = 0
while True:  # flag: ponto de parada (bandeira de parada)
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')


