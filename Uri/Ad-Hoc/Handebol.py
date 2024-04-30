def the_best(dados):
    count = 0
    for dd in dados:
        pc = True
        for d in dd:
            if d == 0:
                pc = False
                break
            
        if pc:
            count+=1
        
    return count

dados = []
nm = list(map(int, input().split()))
for _ in range(nm[0]):
    dados.append(list(map(int, input().split())))

print(the_best(dados))