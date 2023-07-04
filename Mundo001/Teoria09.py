#                   Manipulando Texto
# string: cadeia de texto
# para o Python toda cadeia de texto está entre aspas simples ou duplas
# 'Curso em Vídeo Python'
# frase = 'Curso em Vídeo Python'
# essa frase entra para a memória do computador
# O python cria miniespaços na memória do computador
# e em cada miniespaço entram os caracteres
# e cada miniespaço recebe um índice
# [C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í]  [d]  [e]  [o]  [ ]  [P]  [y]  [t]  [h]  [o]  [n]
# [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]
# 0 - 20 caracteres
# 21 caracteres

#                   Operações
#                   Fatiamento
# frase[9] --> identifica o caractere correspondente ao índice 9 [V]
# símbolo de colchetes: identificador de listas

#               Outras formas de fatiamento de string

# frase[9:13] --> começa no índice 9 até o 12, sim, até o 12 (sempre pega um índice a menos no final)
# [V] [í]  [d]  [e]
# [9] [10] [11] [12]
# [9:13] isso se chama 'range': serve para documentar intervalos númericos

# frase[9:21] --> começa no índice 9 até o 20
# [V] [í]  [d]  [e]  [o]  [ ]  [P]  [y]  [t]  [h]  [o]  [n]
# [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]

# frase[9:21:2] --> começa no índice 9 até o 20, pulando a cada 2
# [V] [d]  [o]  [P]  [t]  [o]
# [9] [11] [13] [15] [17] [19]
# frase[início: fim+1 : pulos]

# se você omitir o início ele começa do índice 0
# frase[:5] --> começa do índice 0 e termina no 4
# [C] [u] [r] [s] [o]
# [0] [1] [2] [3] [4]

# início indicado, mas sem o final: o python entende como se fosse até o último índice
# frase[15:] --> começa no índice 15 e vai até o último índice
# [P]  [y]  [t]  [h]  [o]  [n]
# [15] [16] [17] [18] [19] [20]

# início indicado, sem final, e pulos indicados: o python entende que o final não indicado,
# significa que vai até o último índice
# frase[9::3] --> começa no índice 9 até o último índice, pulando a cada 3
# [V] [e]  [P]  [h]
# [9] [12] [15] [18]

#                   Análise
# len(frase) --> comprimento da variável frase
# 21 carcateres

# frase.count('o') --> conte quantos 'o' existem
# 4 caracteres

# frase.count('o', 0, 13) --> contagem com fatiamente
# conta do índice 0 ao 12, quantos caracteres 'o' existem
# 1 caractere

# frase.find('deo') --> vai mostrar a posição em que 'deo' foi encontrado
# posição 11 (começa em 11)

# frase.find('Android')
# se não for encontrado na frase
# posição -1 --> não existe, não foi encontrado

# 'Curso' in frase --> na frase existe a palavra 'Curso'?
# se sim, 'True'
# se não, 'False'

#                   Transformação

# frase.replace('Python', 'Android') --> trocar/reposicionar
# onde tiver escrito 'Python' será substituído por 'Android'
# [C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í]  [d]  [e]  [o]  [ ]  [A]  [n]  [d]  [r]  [o]  [i] [d]

# frase.upper() --> mantêm o que é maiúsculo e substitui o restante para maiúsculo
# [C] [U] [R] [S] [O] [ ] [E] [M] [ ] [V] [Í]  [D]  [E]  [O]  [ ]  [P]  [Y]  [T]  [H]  [O]  [N]

# frase.lower() --> mantêm o que é minúsculo e substitui o restante para minúsculo
# [c] [u] [r] [s] [o] [ ] [e] [m] [ ] [v] [í]  [d]  [e]  [o]  [ ]  [p]  [y]  [t]  [h]  [o]  [n]

# frase.capitalize() --> toda a frase ficará em minúsculo
# e somente o primeiro caractere em maiúsculo
# [C] [u] [r] [s] [o] [ ] [e] [m] [ ] [v] [í]  [d]  [e]  [o]  [ ]  [p]  [y]  [t]  [h]  [o]  [n]

# frase.title() --> quebra as palavras pelos espaços
# cada palavra com somente a primeira letra maiúscula
# [C] [u] [r] [s] [o] [ ] [E] [m] [ ] [V] [í]  [d]  [e]  [o]  [ ]  [P]  [y]  [t]  [h]  [o]  [n]

# Nova frase
# [ ] [ ] [ ] [A] [p] [r] [e] [n] [d] [a] [ ]  [P]  [y]  [t]  [h]  [o]  [n]  [ ]  [ ]
# [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18]

# frase.strip() --> remove espaços inúteis no início e no fim
# [A] [p] [r] [e] [n] [d] [a] [ ] [P]  [y]  [t]  [h]  [o]  [n]
# [0] [1] [2] [3] [4] [5] [6] [7] [8]  [9]  [10] [11] [12] [13]

# frase.rstrip() --> r: right, remove os espaços vazios somente do lado direito
# [ ] [ ] [ ] [A] [p] [r] [e] [n] [d] [a] [ ]  [P]  [y]  [t]  [h]  [o]  [n]
# [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16]

# frase.lstrip() --> l: left,  remove os espaços vazios somente da esquerda
# [A] [p] [r] [e] [n] [d] [a] [ ]  [P]  [y]  [t]  [h]  [o]  [n]  [ ]  [ ]
# [0] [1] [2] [3] [4] [5] [6] [7]  [8]  [9]  [10] [11] [12] [13] [14] [15]

#             frase:
# [C] [u] [r] [s] [o] [ ] [e] [m] [ ] [V] [í]  [d]  [e]  [o]  [ ]  [P]  [y]  [t]  [h]  [o]  [n]
# [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15] [16] [17] [18] [19] [20]

#                      Divisão
# frase.split() --> divide considerando os espaços
# cada palavra recebe uma nova indexação sendo colocada numa nova lista
# [C] [u] [r] [s] [o]   [e] [m]   [V] [í] [d] [e] [o]    [P] [y] [t] [h] [o] [n]
# [0] [1] [2] [3] [4]   [0] [1]   [0] [1] [2] [3] [4]    [0] [1] [2] [3] [4] [5]
#        [0]              [1]            [2]                        [3]

#                    Junção
# '-'.join(frase) --> juntar todos os elementos de frase (0, 1, 2, 3)
# ultilizando o separador determinado
# [C] [u] [r] [s] [o] [-] [e] [m] [-] [V] [í]  [d]  [e]  [o]  [-]  [P]  [y]  [t]  [h]  [o]  [n]


