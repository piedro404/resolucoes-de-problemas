primes = [2, 3, 5, 7]
for mask in range(1, 1 << 4): 
    subset = []
    for i in range(4):
        if (mask >> i) & 1:
            subset.append(primes[i])
    
    print(*subset)