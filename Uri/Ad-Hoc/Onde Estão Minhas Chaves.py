dados = list(map(int, input().split()))
isVisit = list(map(int, input().split()))
for x in range(dados[0]):
    x = int(input())
    if x in isVisit:
        print(0)
    else:
        print(1)
        isVisit.append(x)