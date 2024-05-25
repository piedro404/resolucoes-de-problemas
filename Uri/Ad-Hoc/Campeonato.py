def pontosTotal(vit, emp):
    return vit * 3 + emp

def vitoria(c, f):
    pC = pontosTotal(c[0], c[1])
    pF = pontosTotal(f[0], f[1])
    
    if pC == pF:
        if c[2] == f[2]:
            return "="
        elif c[2] > f[2]:
            return "C"
        
        return "F"
    
    elif pC > pF:
        return "C"
    
    return "F"

dados = list(map(int, input().split()))
c = dados[0:3]
f = dados[3:6]
print(vitoria(c, f))