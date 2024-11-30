import math

while True:
    try:
        M, N = map(int, input().split())
        M = math.factorial(M)
        N = math.factorial(N)

        print(M+N)
    except EOFError:
        break