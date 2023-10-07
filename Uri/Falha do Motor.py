def testes(rpms):
    for x in range(1, len(rpms)):
        if rpms[x-1] > rpms[x]:
            return x+1
    
    return 0

int(input())
dados = list(map(int, input().split()))
print(testes(dados))