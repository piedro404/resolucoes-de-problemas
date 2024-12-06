for _ in range(int(input())):
    dados = list(map(int, input().split()))
    count=0
    media = sum(dados[1::]) / dados[0]

    for x in dados[1::]:
        if x > media:
            count+=1

    print(f"{(count/dados[0]*100):.3f}%")