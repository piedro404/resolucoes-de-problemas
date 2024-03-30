def moeda(dados):
    mary = len([x for x in dados if x==0])
    john = len(dados) - mary
    
    return f"Mary won {mary} times and John won {john} times"

while True:
    x = int(input())
    if x == 0:
        break
    dados = list(map(int, input().split()))
    print(moeda(dados))