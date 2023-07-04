# Refaça o desafio 009, mostrando a tabuada de um
# número que o usuário escolher, contudo, agora
# utilizando um laço for.

print(f'{" Desafio 009 ":=^30}')
print(f'{" Desafio 049 ":*^30}')
num = int(input('Digite um número para obter a tabuada: '))
print(f'{f" Tabuada {num} ":*^30}')
for i in range(11):
    print(f'{num} x {i:2} = {num*i}') 
