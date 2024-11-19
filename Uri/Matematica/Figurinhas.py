import math

for _ in range(int(input())):
    F1, F2 = map(int, input().split())

    print(math.gcd(F1, F2))