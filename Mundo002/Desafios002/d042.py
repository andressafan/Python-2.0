# Refaça o desafio 035 dos triângulos, acrescentando o rescurso
# de mostrar a categoria de triângulo que será formado:

# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print(f'{"Desafio 035":=^30}')
print(f'{"Desafio 042":*^30}')
l1 = int(input('Digite o tamanho do primeiro lado: '))
l2 = int(input('Digite o tamanho do segundo lado: '))
l3 = int(input('Digite o tamanho do terceiro lado: '))
if l3 - l2 < l1 < l3 + l2 and l1 - l3 < l2 < l1 + l3 and l1 - l2 < l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Triângulo Equilátero')
    elif l1 == l2 or l3 == l1 or l3 == l2:
        print('Triângulo Isósceles')
    elif l1 != l2 != l3:
        print('Triângulo Escaleno')
else:
    print('Não é triâgulo!')
