def resultCha(t, dados):
    return dados.count(t)

t = int(input())
dados = list(map(int, input().split()))
print(resultCha(t, dados))