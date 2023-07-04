# Faça um programa que leia o nome
# completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.

print(f'{"Desafio 027":=^30}')
nome = input('Digite seu nome: ').strip()
div = nome.split()
print(f'''O primeiro nome: {div[0]}
O último nome: {div[-1]}''')
