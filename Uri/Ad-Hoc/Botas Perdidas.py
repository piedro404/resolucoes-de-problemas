while True:
    try:
        botas = {}

        for _ in range(int(input())):
            dados = input().split()
            try:
                if dados[1] == "E":
                    botas[dados[0]][0] += 1
                else:
                    botas[dados[0]][1] += 1
            except:
                botas[dados[0]] = [0, 0]
                if dados[1] == "E":
                    botas[dados[0]][0] = 1
                else:
                    botas[dados[0]][1] = 1

        pares = 0
        for b in botas:
            pares += min(botas[b])

        print(pares)
    except EOFError:
        break