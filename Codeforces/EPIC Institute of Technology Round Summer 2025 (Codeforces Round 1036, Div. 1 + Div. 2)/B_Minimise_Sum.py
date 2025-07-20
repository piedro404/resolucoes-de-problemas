for _ in range(int(input())):
    n = int(input())
    lista = list(map(int, input().split()))

    if n == 2:
        print(lista[0] + min(lista[0], lista[1]))

    else:
        print(min(
            lista[0] + lista[1],
            lista[0] + min(lista[0], lista[1] + lista[2]),
            lista[0] + min(lista[0], lista[1]) + min(lista[0], lista[1], lista[2])
        ))