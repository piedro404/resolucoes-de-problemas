i = 1
while True:
    x = int(input())
    if x == 0:
        break
    print(f"Teste {i}")
    dif = 0
    for _ in range(x):
        n1, n2 = map(int, input().split())
        dif += n1 - n2
        print(dif)
    print()
    i+=1
    