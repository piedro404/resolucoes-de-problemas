while True:
    x = int(input())
    if x == 0:
        break

    vez = 0
    order = list(range(1, x + 1))
    while True:
        vez += 1
        dados = list(map(int, input().split()))
        if dados == order:
            break
    print(vez)