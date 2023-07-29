# Funções

# Rotina
# def -> usado para declarar uma função personalizada

# print('-----------------------------') ---> se repete
# print('Sistema de Alunos')
# print('-----------------------------')

# print('-----------------------------')
# print('Cadastro de Funcionários')
# print('-----------------------------')

# print('-----------------------------')
# print('Erro do Sistema')
# print('-----------------------------')


# def mostraLinha(): --> função é definida
#   print('-----------------------------')


# mostraLinha() --> função é chamada
# print('Sistema de Alunos')
# mostraLinha()
# print('Cadastro de Funcionários')
# mostraLinha()
# print('Erro do Sistema')
# mostraLinha()

# a função deve ser chamada para ser executada!


# Ultilizando Parâmetros:

# def mensagem(msg): ---> msg = parâmetro
#   print('-----------------------------')
#   print(msg)
#   print('-----------------------------')

# mensagem('Sistema de Alunos') --> chama a função e passa o parâmetro

# Empacotamento de Parâmetros:

# def contador(*núm): ---> * = recebe vários parâmetros


# contador(5, 7, 3, 4)
# contador(8, 9, 7)

# Trabalhando com Listas:

# def dobra(lst):
#   pos = 0
#   while pos < len(lst):
#       lst[pos] *= 2
#       pos += 1

# valores = [7,2,5,0,4]
# dobra(valores)
# print(valores)
