# 1387
def soma(dados):
    return(dados[0]+dados[1])

while True:
    dados = list(map(int, input().split()))
    if dados[0] == dados[1] == 0:
        break
    
    print(soma(dados))