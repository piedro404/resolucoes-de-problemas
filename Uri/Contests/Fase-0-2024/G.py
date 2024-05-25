def saci(x, t, lojas, qtdT):
    p = 0
    i = 0
    dbT = t
    while i < x:
        if lojas[i] <= t:
            if dbT < lojas[i] + qtdT[i]:
                dbT = lojas[i] + qtdT[i]
        else:
            t = dbT
            p+=1
            if lojas[i] > t:
                return -1
            else:
                i -= 1
        
        i+=1  
        
    return p

x, t = map(int, input().split())
lojas = list(map(int, input().split()))
qtdT = list(map(int, input().split()))

print(saci(x, t, lojas, qtdT))