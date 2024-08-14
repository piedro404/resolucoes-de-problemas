import math

def festa(n):
    cor = None
    custo = 0
    r = math.sqrt((n/(3.14*4)))

    if r < 12:
        cor = "vermelho"
        custo = n*0.09
    elif r >= 12 and r <= 15:
        cor = "azul"
        custo = n*0.07
    else:
        cor = "amarelo"
        custo = n*0.05
    

    return f"{cor} = R$ {custo:.2f}"

for _ in range(int(input())):
    print(festa(int(input())))

