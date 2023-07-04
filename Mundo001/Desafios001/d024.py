# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

print(f'{"Desafio 024":=^30}')
cidade = (input('Digite o nome da sua cidade: ')).upper().strip()
div = cidade.split()
if 'SANTO' in div[0]:
    print('Santo é o primeiro nome da sua cidade!')
else:
    print('Santo não é o primeiro nome de sua cidade!')

'''cidade = (input('Digite o nome da sua cidade: ')).upper().strip()
print(cidade[:5] == 'SANTO')'''