def respT(list):
    i = list.index(min(list))
    return i+1

int(input())
dados = list(map(int, input().split()))
print(respT(dados))