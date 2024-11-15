def knapSack(capacity, weights, values, n):
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    result = K[n][capacity]

    w = capacity
    items_chosen = []
    for i in range(n, 0, -1):
        if result <= 0:
            break
        if result == K[i - 1][w]:
            continue
        else:
            items_chosen.append(i - 1)
            result -= values[i - 1]
            w -= weights[i - 1]

    return K[n][capacity], items_chosen


for _ in range(int(input())):
    weights = []
    values = []
    for _ in range(int(input())):
        item = list(map(int, input().split()))
        values.append(item[0])
        weights.append(item[1])

    result = knapSack(50, weights, values, len(weights))
    total = 0
    for x in result[1]:
        total += weights[x]
    print(f"{result[0]} brinquedos")
    print(f"Peso: {total} kg")
    print(f"sobra(m) {len(weights)-len(result[1])} pacote(s)")
    print()