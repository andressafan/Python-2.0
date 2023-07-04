print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[4;30;45mOlá, mundo!\033[m')
print('\033[30mOlá, mundo!\033[m')
print('\033[0;33;44mOlá, mundo!\033[m')
print('\033[7;33;44mOlá, mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')
nome = 'Guanabara'
print('Olá! Muito prazer em te conhece, {}{}{}!!!'.format("\033[4:35m", nome, "\033[m"))
nome = 'Guanabara'
cores = {'limpa': '\033[m',  # dicionário
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30m'}
print('Olá! Muito prazer em te conhece, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
