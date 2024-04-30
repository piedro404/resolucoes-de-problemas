def voltas(dados):
    if dados[0] > dados[1]:
        min = dados[1]
        max = dados[0]
    else:
        min = dados[0]
        max = dados[1]
        
    i = 0
    v = 0
    while True:
        if min*i <= (max*i)-max:
            break
        i+=1
        v+=1
        
    return v
    
print(voltas(list(map(int, input().split()))))