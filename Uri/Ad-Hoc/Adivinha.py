def adivinha(n, dados):
    mI = 0
    mAbs = abs(dados[0]-n)
    for x in range(1, len(dados)):
        cAbs = abs(dados[x]-n) 
        if cAbs < mAbs:
            mI = x
            mAbs = cAbs
            
    return mI + 1

for _ in range(int(input())):
    i, n = map(int, input().split())
    dados = list(map(int, input().split()))
    print(adivinha(n, dados))