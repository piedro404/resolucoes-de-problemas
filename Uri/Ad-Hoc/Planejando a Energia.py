for _ in range(int(input())):
    dados = list(map(int, input().split()))
    anosDif = abs(dados[2]-dados[0])
    volt = abs(dados[3]-dados[1])
    result = str("{:.3f}".format(volt/anosDif)).replace('.', ',')
    print(result[0:-1])

