for _ in range(int(input())):
    dados = list(map(int, input().split()))
    ele = (dados[0]**dados[1])
    print(len(str(ele)))