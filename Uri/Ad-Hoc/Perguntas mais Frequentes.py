while True:
    dados = list(map(int, input().split()))
    if dados[0] == dados[1] == 0:
        break
    qtdFreq = 0
    dic = {}
    for x in list(map(int, input().split())):
        try:
            dic[x] += 1
        except:
            dic[x] = 1
            
        if dic[x] == dados[1]:
            qtdFreq+=1
    print(qtdFreq)

