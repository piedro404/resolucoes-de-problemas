from itertools import combinations

primes = [2, 3, 5, 7]

for k in range(1, len(primes)+1): 
    for subset in combinations(primes, k):
        print(list(subset))
