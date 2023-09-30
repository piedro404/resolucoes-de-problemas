def tentativa(name, n):
    if name == "Thor":
        return "Y"
    
    return "N"

for _ in range(int(input())):
    dados = list(input().split())
    print(tentativa(dados[0], dados[1]))