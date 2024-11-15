def knapSack(capacity, weights, values, n):
    if n == 0 or capacity == 0:
        return 0

    if (weights[n-1] > capacity):
        return knapSack(capacity, weights, values, n-1)

    else:
        return max(
            values[n-1] + knapSack(
                capacity-weights[n-1], weights, values, n-1),
            knapSack(capacity, weights, values, n-1))
    
values = [10, 40, 15, 90]
weights = [1, 1, 2, 4]
capacity = 4
n = 4

print(knapSack(capacity, weights, values, n))

