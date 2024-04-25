def escada_rolante(dados):
    time = 0
    ant = dados[0]-10-1
    for x in dados:
        if ant+10 < x:
            time += 10
        else:
            time += x-ant    
        
        ant = x
        
    return time

while True:
    n = int(input())
    if n == 0: 
        break
    dados = list(map(int, input().split()))
    print(escada_rolante(dados))