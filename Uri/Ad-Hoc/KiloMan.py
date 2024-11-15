for _ in range(int(input())):
    int(input())
    tiros = list(map(int, input().split()))
    acao = str(input())
    acertos = 0

    for x in range(len(acao)):
        if acao[x] == "J":
            if tiros[x] > 2:
                acertos +=1
        else:
            if tiros[x] < 3:
                acertos +=1

    print(acertos)