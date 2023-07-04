n1 = input('Digite um valor: ')
print(type(n1))
# Pode ver o tipo primitivo através de type
# str

n1 = int(input('Digite um valor: '))
print(type(n1))
# int

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

# Testanto tipos primitivos
n = float(input('Digite um valor: '))
print(n)
# veja que o tipo primitivo formata de acordo com o seu uso
n = bool(input('Digite um valor: '))
print(n)
# True
# Têm um valor dentro? True
# caso não tenha nenhum valor: False

# Método isnumeric
# teste de tipo
n = input('Digite algo: ')
print(n.isnumeric())
# funciona para saber se dá para converter algo para o padrão numérico,
# ou seja, se é possível converter algo para número com o tipo primitivo (int) antes dele;
n = input('Digite algo: ')
print(n.isalpha())
# para saber se é letra
