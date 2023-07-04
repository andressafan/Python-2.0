# Cores no Terminal
# ANSI — escape sequence
# sempre que for representar uma cor em python

# use \033['código da cor'm
#      style text back
# \033[  0  : 33:  44m
#  Style         Text        Back
#  0 none        30 white    40 white
#  1 bold        31 red      41 red
#  4 underline   32 green    42 green
#  7 negative    33 yellow   43 yellow
#                34 blue     44 blue
#                35 purple   45 purple
#                36 cyan     46 cyan
#                37 gray     47 gray

# sem formatação, texto em branco, e fundo vermelhor \033[0:30:41m
# sublinhado, texto amarelo, fundo azul \033[4:33:44m
# negrito, texto roxo, fundo amarelo \033[1:35:43m
# sem formatação, texto branco, fundo verde \033[30:42m
# sem formatação, texto branco, fundo preto \033[m (padrão)
# sem formatação, texto preto, fundo branco \033[7:30m
