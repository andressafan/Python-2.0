# Faça um programa que calcule a soma entre todos
# os números ímpares que são múltiplos de três e
# no intervalo de 1 até 500.

print(f'{" Desafio 048 ":=^30}')
s = 0  # acumulador
c = 0  # contador
for i in range(1, 501, 2):
    if i % 3 == 0:
        c += 1
        s += i
print(f'A soma de todos os {c} valores solicitados é {s}')
