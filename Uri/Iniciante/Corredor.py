def vidas(n, vidas):

    max_atual = max_total - vidas[0]

    for i in range(i, n):

        max_atual = max(vidas[i], max_atual + vidas[i])
        max_total = max(max_total, max_atual)

    return max_total

n = int(input())

vidas = list(map(int, input().split()))

resultado = vidas(n, vidas)

print(resultado)