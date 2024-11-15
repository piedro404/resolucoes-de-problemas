while True:
    n = int(input())
    if n == 0:
        break
    
    dados = list(map(int, input().split()))

    lenT = len(dados)
    pontas = 0
    for x in range(0, lenT):
        if lenT-1 != x:
            if dados[x-1] < dados[x] > dados[x+1]:
                pontas +=1
        elif lenT-1 == x:
            if dados[x-1] < dados[x] > dados[0]:
                pontas +=1
        else:
            if dados[-1] < dados[x] > dados[x+1]:
                pontas +=1

    print(pontas*2)
