def fazenda(area, testes):
    x = [area[0], area[2]]
    y = [area[1], area[3]]
    x.sort()
    y.sort()

    m = 0
    for teste in testes:
        if (teste[0] >= x[0] and teste[0] <= x[1]) and (teste[1] >= y[0] and teste[1] <= y[1]):
            m+=1
    
    return m
    
i=1
while True:
    dados = list(map(int, input().split()))
    if dados == [0, 0, 0, 0]:
        break
    testes=[]
    for _ in range(int(input())):
        testes.append(list(map(int, input().split())))

    print(f"Teste {i}")
    print(fazenda(dados, testes))
    i+=1

    