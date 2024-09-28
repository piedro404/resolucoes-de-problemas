x = int(input())
has = set(list(map(int, input().split())))

for n in range(1, x+1):
    if n not in has:
        print(n)
        break

