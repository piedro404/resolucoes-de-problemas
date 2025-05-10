notas = [100, 50, 20, 10, 5, 2, 1]
N = int(input())

print(N)
for x in notas:
    print(f"{N//x} nota(s) de R$ {x},00")
    N = N % x