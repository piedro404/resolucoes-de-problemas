def tomada(n, s):
    return (s-(n-1))

for _ in range(int(input())):
    dados = list(map(int, input().split()))
    print(tomada(dados[0], sum(dados[1::])))