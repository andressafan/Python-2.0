# Crie um programa que leia duas notas de um aluno e calcule
# a sua média, mostrandono final, conforme a média atingida:

# — Média abaixo de 5,0: REPROVADO
# — Média entre 5,0 e 6,9: RECUPERAÇÃO
# — Média 7,0 ou superior: APROVADO

print(f'{"Desafio 040":=^30}')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print(f'Tirando {n1:.1f} e {n2:.1f} a média fica: {m:.1f}')
    print('REPROVADO')
elif 5.0 <= m < 6.9:
    print(f'Tirando {n1:.1f} e {n2:.1f} a média fica: {m:.1f}')
    print('RECUPERAÇÃO')
else:
    print(f'Tirando {n1:.1f} e {n2:.1f} a média fica: {m:.1f}')
    print('APROVADO')
