def opcao(dados):
    s = sum(dados)
    op = ["PROXYCITY", "P.Y.N.G.", "DNSUEY!", "SERVERS", "HOST!", "CRIPTONIZE", "OFFLINE DAY", "SALT", "ANSWER!", "RAR?", "WIFI ANTENNAS"]
    return op[s]

for _ in range(int(input())):
    dados = list(map(int, input().split()))
    print(opcao(dados))