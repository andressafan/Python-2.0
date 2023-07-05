'''Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores "M" ou "F". Caso esteja errado, peça
a digitação novamente até ter um valor correto'''

print(f'{" Desafio 057 ":=^30}')

nome = str(input('Digite seu nome: '))
sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Valor inválido! Digite novamente: ')).upper()

print(f'''Cadastro:
      nome: {nome}
      sexo: {'Feminino' if sexo == "F" else 'Masculino'}''')
