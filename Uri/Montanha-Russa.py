while True:
    try:
        dados = list(map(int, input().split()))
        count = 0

        for _ in range(dados[0]):
            alt = int(input())

            if dados[1] <= alt and dados[2] >= alt:
                count+=1

        print(count)
    except EOFError:
        break