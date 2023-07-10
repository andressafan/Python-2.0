"""
Crie um programa onde o usuário digite uma expressão
qualquer que use parêntese. Seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos e fechados
na ordem correta.
"""
print(f'{" Desafio 083 ":=^50}')
'''e = str(input('Digite uma expressão algébrica (com parênteses): '))

lista = []
while '(' in e or ')' in e:
    e = ''.join(e.split())  # Remove espaços em branco da expressão
    for i in range(len(e)):
        # ['a', '+', 'b', ')']  [3]
        # [ 0,   1 ,  2 ,  3 ]
        if '(' in e:
            for pos in range(i + 1, len(e)):
                if ')' not in e[pos]:
                    lista.append(0)
        #     ['a', '+', 'b', ')']
        # ]-1[[ 0,   1 ,  2 ,  3 ]
        if ')' in e:
            for posicao in range(len(e) - i - 1, -1, -1):
                if '(' not in e[posicao]:
                    lista.append(1)
    if 0 in lista or 1 in lista:
        print('Inválido')
        break
# não deu certo'''

e = str(input('Digite uma expressão algébrica (com parênteses): '))

pilha = []
valido = True

for char in e:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            valido = False
            break

if valido and len(pilha) == 0:
    print('Válido')
else:
    print('Inválido')

print('='*50)
print('Forma que o Guanabara fez: ')
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
