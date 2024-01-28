def isVale(dados):
    if dados[0] == dados[1]:
        return 0
    
    seq=-1
    for x in range(1, len(dados)):
        p = dados[x-1]
        seqP = (0 if p > dados[x] else 1)
        if seq == seqP or p == dados[x]:
            return 0
        
        seq = seqP

    return 1

int(input())
dados = list(map(int, input().split()))
print(isVale(dados))