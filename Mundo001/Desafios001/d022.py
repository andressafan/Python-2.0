# Crie um programa que leia o nome completo de uma
# pessoa e mostre:

# --> O nome com todas as letras maiúsculas
# --> O nome com todas minúsculas
# --> Quantas letras ao toodo (sem considerar espaços)
# --> Quanras letras tem o primeiro nome

print(f'{"Desafio 022":=^30}')
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
div = nome.split()
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome é: {div[0]} e tem {len(div[0])} letras')
