def ciclos(hist, lenC):
    qtdCiclos = 0
    countR = 0
    for h in hist:
        if h == "W":
            qtdCiclos += 1
            countR = 0
        else:
            if countR == 0:
                qtdCiclos+=1
            countR +=1
            if countR == lenC:
                countR = 0
                
    return qtdCiclos

while True:
    try:
        hist = str(input())
        n = int(input())
        print(ciclos(hist, n))
    except EOFError:
        break
    