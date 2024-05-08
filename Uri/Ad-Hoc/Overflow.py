def calOver(dados):
    if dados[1] == "+":
        return int(dados[0])+int(dados[2])
    if dados[1] == "-":
        return int(dados[0])-int(dados[2])
    if dados[1] == "*":
        return int(dados[0])*int(dados[2])

    return int(dados[0])/int(dados[2])

def overflow(dados, n):
    if calOver(dados) > n:
        return "OVERFLOW"
    
    return "OK"

n = int(input())
dados = list(map(str, input().split()))
print(overflow(dados, n))
