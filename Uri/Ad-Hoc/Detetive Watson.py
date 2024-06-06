def SMaior(n, dados):
    idcM = 0
    idcM2 = n-1
    for x in range(1, n):
        if dados[idcM] < dados[x]:
            idcM2 = idcM
            idcM = x
        elif dados[idcM] >  dados[x] > dados[idcM2]:
            idcM2 = x
            
    return idcM2+1

while True:
    n = int(input())
    if n == 0:
        break
    dados = list(map(int, input().split()))
    print(SMaior(n, dados))
