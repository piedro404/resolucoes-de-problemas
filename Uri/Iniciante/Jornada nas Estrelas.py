def jornadasNasEstrelas(carneiros):
    inv = 0
    totalCarneiros = sum(carneiros)

    i=0
    while i>=0 and i<len(carneiros):
        c=0
        if carneiros[i] % 2 != 0:
            c = 1
        else:
            c = -1

        if carneiros[i] > 0:
            totalCarneiros -= 1
            carneiros[i] -= 1
        
        if i > inv:
            inv = i

        i+=c

        

    return inv+1, totalCarneiros

int(input())
dados = list(map(int, input().split()))
inv, totalRestante = jornadasNasEstrelas(dados)
print(inv, totalRestante)
