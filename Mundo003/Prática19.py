pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5  # não precisa de append
for k, v in pessoas.items():
    print(f'{k} = {v}')

# dicionário dentro de uma lista

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)  # lista com dicionários
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    # brasil.append(estado[:])  # como fazer a cópia do estado para colocar na lista sem fazer fatiamento?
    brasil.append(estado.copy())  # assim (copy)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

