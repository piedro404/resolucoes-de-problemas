valorGoverno = 0
gastoUniver = 0

for _ in range(int(input())):
    dados = list(input().split())
    v = int(dados[1])
    if dados[0] == "V":
        valorGoverno += v
    else:
        gastoUniver += v

if valorGoverno >= gastoUniver:
    print("A greve vai parar.")
else:
    print("NAO VAI TER CORTE, VAI TER LUTA!")