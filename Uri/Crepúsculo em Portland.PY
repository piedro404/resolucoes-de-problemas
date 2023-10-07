def cam(quadra):
    c = 0
    for x in quadra:
        c+= x.count(1)
    if c > 1:
        return "S"

    return "U"

def analiseQ(quadras):
    secQs = []
    for x in range(len(quadras)-1):
        secQ = []
        for y in range(len(quadras[x])-1):
            secQ.append(cam([[quadras[x][y], quadras[x][y+1]], [quadras[x+1][y], quadras[x+1][y+1]]]))

        secQs.append(secQ)

    return secQs

def printAnalise(secQs):
    for x in secQs:
        for y in x:
            print(y, end="")
        print()

n = int(input())
quadras = []
for x in range(n+1): 
    quadras.append(list(map(int, input().split())))

printAnalise(analiseQ(quadras))