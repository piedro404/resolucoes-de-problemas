def restante(dados):
    ped = 0
    for x in dados:
        ped += x-1
        
    return ped

int(input())
print(restante(list(map(int, input().split()))))