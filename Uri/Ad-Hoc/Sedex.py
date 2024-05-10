def cabe(dados, n):
    for x in dados:
        if x < n:
            return "N"
        
    return "S"

n = int(input())
dados = list(map(int, input().split()))
print(cabe(dados, n))