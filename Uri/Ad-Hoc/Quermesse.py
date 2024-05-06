def sortudo(dados):
    for x in range(len(dados)):
        if dados[x] == x+1:
            return dados[x]
    
    return -1

i = 1
while True:
    n = int(input())
    if n==0:
        break
    
    print(f"Teste {i}")
    print(sortudo(list(map(int, input().split()))))
    print()
    i+=1