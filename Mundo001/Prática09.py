frase = '   Curso em Vídeo Python'
print(frase)
# fatiamento
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[0::4])
print(frase[::2])
# três aspas duplas ou simples para textos longos
print('''Nada do que é social e humano é mais real que as utopias.
Na sua vertente eutópica, as utopias constituíram sempre o fundamento simbólico e mítico 
sem o qual nenhuma forma de organização social se sustenta, justifica ou sobrevive.''')
print(frase.upper().count('o'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
# replace não muda efetivamente a frase, é como se so criasse uma máscara
# veja
print(frase)
# para mudar mesmo:
frase = frase.replace('Python', 'Android')
print(frase)
print('Curso' in frase)
# A palavra 'Curso' está em frase?
print(frase.lower().find('vídeo'))
# qual a posição de 'vídeo' em frase?
# (tendo a frase sido convertido para minúsculo {lower})
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[0][3])
# dentro do dividido [0] --> 'Curso' mostre a letra [3] --> 's'
