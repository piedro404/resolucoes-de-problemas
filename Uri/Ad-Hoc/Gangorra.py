def corda(dados):
    p1 = dados[0]*dados[1]
    p2 = dados[2]*dados[3]
    
    if p1==p2:
        return "0"
    
    elif p1 < p2:
        return "1"
    
    return "-1"

dados = list(map(int, input().split()))
print(corda(dados))