def sequencia(dados):
    listf = ""

    for x in range(dados[0], dados[1]+1):
        listf += (str(x))

    listr = listf[::-1]

    return listf+listr

for _ in range(int(input())):
    print(sequencia(list(map(int, input().split()))))