def quantas_garrafas(dados):
    trade = dados[0]//dados[1]
    if trade == 0:
        return dados[0]
    
    return trade + dados[0]%dados[1]

for _ in range(int(input())):
    print(quantas_garrafas(list(map(int, input().split()))))