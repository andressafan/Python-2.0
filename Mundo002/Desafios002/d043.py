# Desenvolva uma lógica qye leia o peso e a altura
# de uma pessoa, calcule o seu IMC e mostre o seu status, conforme
# a tabela abaixo:

# - Abaixo de 18.5: Abaixo do Peso ideal
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print(f'{"Desafio 043":=^30}')
p = float(input('Digite seu peso em kg: '))
h = float(input('Digite sua altura em m: '))
imc = p / (h ** 2)
print(f'IMC = {imc:.1f}')
if imc < 18.5:
    print('Cuidado! Você está abaixo do seu peso ideal, cuide de sua saúde!')
elif 18.5 <= imc < 25:
    print('Você está no seu peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está obeso!')
else:
    print('Cuidado! Você está com obesidade mórbita, cuide de sua saúde!')