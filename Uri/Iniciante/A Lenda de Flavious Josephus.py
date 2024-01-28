def josephus(n, k):
    survivor = 1
    for i in range(2, n + 1):
        survivor = (survivor + k - 1) % i + 1
    return survivor

nc = int(input())

for x in range(nc):
    n, m = map(int, input().split())
    result = josephus(n, m)
    print(f"Case {x+1}: {result}")