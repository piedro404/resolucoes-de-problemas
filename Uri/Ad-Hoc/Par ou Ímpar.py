i = 0
while True:
    x = int(input())
    if x == 0:
        break
    i+=1
    print(f"Teste {i}")
    parN = str(input())
    imparN = str(input())

    for _ in range(x):
        if(sum(list(map(int, input().split()))) % 2 == 0):
            print(parN)
        else:
            print(imparN)
    print()