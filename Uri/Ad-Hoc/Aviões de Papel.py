def aviao_papel(dados):
    if dados[0]*dados[2] <= dados[1]:
        return "S"
    
    return "N"

print(aviao_papel(list(map(int, input().split()))))