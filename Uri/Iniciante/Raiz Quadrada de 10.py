def func(n):
    if n == 0:
        return 3
    
    den = 0
    for _ in range(n):
        den = 6 + 1 / den if den != 0 else 6
    
    return 3 + 1 / den

n = int(input())
print("{:.10f}".format(func(n)))
