def coral(ind, somaTotal, n):
    if(somaTotal%n != 0):
        return -1
    
    comp = 0
    somaTotal = somaTotal/n
    i=0
    while i<n:
        if ind[i] > somaTotal:
            comp += ind[i] - somaTotal
        i+=1
    
    return int(comp+1)

while True:
    try:
        n = int(input())
        dados = list(map(int, input().split()))
        print(coral(dados, sum(dados), n))
    except EOFError:
        break
