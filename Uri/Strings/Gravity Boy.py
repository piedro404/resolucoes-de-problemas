def gravity(n, teto, chao):
    mimTrocas = 0
    if teto[0] > 0 < chao[0]:
        vezTeto = 0
        vezChao = 0
        posTeto = True
        posChao = True

        for x in range(n-1):
            if teto[x+1] == 0 or teto[x] < teto[x+1]:
                if posTeto:
                    posTeto = False
                    vezTeto +=1
                if not(posChao):
                    posChao = True
                    vezChao +=1
            elif chao[x+1] == 0 or chao[x] < chao[x+1]:
                if not(posTeto):
                    posTeto = True
                    vezTeto +=1
                if posChao:
                    posChao = False
                    vezChao +=1

        if vezChao <= vezTeto:
            mimTrocas = vezChao
        else:
            mimTrocas = vezTeto
    
    else:
        posisao = chao[0] > 0
        for x in range(n-1):
            if teto[x+1] == 0 or teto[x] < teto[x+1]:
                if not(posisao):
                    posisao = True
                    mimTrocas +=1
            elif chao[x+1] == 0 or chao[x] < chao[x+1]:
                if posisao:
                    posisao = False
                    mimTrocas +=1

    return mimTrocas

x = int(input())
teto = list(map(int, input().split()))
chao = list(map(int, input().split()))
print(gravity(x, teto, chao))