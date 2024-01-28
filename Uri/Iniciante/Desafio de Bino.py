def divisores(dados):
    count = [0]*4
    div = [2, 3, 4, 5]
    for d in dados:
        for i, x in enumerate(div):
            if d % x == 0:
                count[i]+=1

    for i, x in enumerate(div):
        print(f"{count[i]} Multiplo(s) de {x}")


int(input())
dados = list(map(int, input().split()))
divisores(dados)