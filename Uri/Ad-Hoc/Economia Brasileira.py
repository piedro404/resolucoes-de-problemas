def economia(n, dados):
    if ((n/2) > (dados.count(1))):
        return "Y"
    
    return "N"

n = int(input())
dados = list(map(int, input().split()))
print(economia(n, dados))