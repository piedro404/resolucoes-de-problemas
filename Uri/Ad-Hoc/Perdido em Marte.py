def sos(dados):
    result = ''
    for x in dados:
        result += chr(int(x, 16))
        
    return result

int(input())
dados = list(map(str, input().split()))
print(sos(dados))
