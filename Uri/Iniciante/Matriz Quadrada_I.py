def matrix(tam):
    for x in range(0, tam):
        linha = []
        for y in range(0, tam):
            linha.append(f"{min(x, y, tam - 1 - x, tam - 1 - y)+1:3}")
        print(" ".join(linha))
    print()

while True:
    n = int(input())

    if n == 0:
        break

    matrix(n)