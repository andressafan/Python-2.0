print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Fim')

for c in range(1, 6):  # do 1 ao 5 (o último número não é considerado)
    print('Oi')
print('Fim')

for c in range(0, 6):
    print('Oi')
print('Fim')

for c in range(0, 6):  # veja que o último índice é ignorado
    print(c)
print('Fim')

for c in range(6, 0):  # Para contar para trás tem que colocar -1 (iteração)
    # vai subtrair um cada laço
    print(c)
print('Fim')

for c in range(0, 7, 2):  # Aqui a interação é pular a cada 2
    print(c)
print('Fim')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')

for c in range(0, 3):  # n será chamado 2 vezes
    n = int(input('Digite um valor: '))
print('Fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')

