# Laços de repetição (parte 1)
# para chegar até a maçã:
# passo
# passo
# passo --> veja que boa parte do programa está se repetindo
# passo
# passo
# pegar maçã

# Estrutura de repetição
# laço --> tudo no laço irá se repetir (‘looping’),
# mas para não executar infinitamente deve
# colocar um limite para o laço
#  passo passo passo passo passo passo passo passo passo passo pegar         *
#   [0]   [1]  [2]   [3]    [4]   [5]  [6]   [7]    [8]   [9]  [10]
# laço de 1 --> 10 (10 - 1: 9) do primeiro índice, até o nono índice

# laço c no intervalo(1, 10)            for c in range(1, 10):
#      passo                                passo
# pegar maçã                            pega

# laço c no intervalo(0, 3)             for c in range(0, 3):
#      passo                                passo
#      pula                                 pula
# passo                                 passo
# pega                                  pega

# laço c no intervalo(0, 3)             for c in range(0, 3):
#   se moeda                                if moeda:
#       pega                                    pega
#   passo                                   passo
#   pula                                    pula
# passo                                 passo
# pega                                  pega
