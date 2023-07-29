def soma(a, b):
    s = a + b
    print(s)


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=3, a=5)


# soma(4) ---> erro! Você tem que passar os parâmetros exigidos pela função

# Empacotamento:

def contador(*núm):
    print(núm)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


# Listas:
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 6, 7, 8, 9]
dobra(valores)
print(valores)
