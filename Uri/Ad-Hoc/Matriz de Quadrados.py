def printTable(tb: list, lenN: list, idx):
    print(f"Quadrado da matriz #{idx}:")
    for x in range(len(tb)):
        p = ""
        for y in range(len(tb)):
            p+= (" "*(lenN[y]-len(tb[x][y])) + tb[x][y])
            if y < len(tb)-1:
                p+=" "
        print(p)

idx = 4
w = int(input())
for ip in range(w):
    tb = []
    x = int(input())
    lenN = [0 for _ in range(x)]
    for x in range(x):
        dados = []
        for i, n in enumerate(input().split()):
            v = str(int(n)**2)
            dados.append(v)
            if lenN[i] < len(v):
                lenN[i] = len(v)

        tb.append(dados)

    printTable(tb, lenN, idx)
    if ip < w-1:
        print()
    idx+=1
    