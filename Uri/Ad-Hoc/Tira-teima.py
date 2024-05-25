def juiz(dados):
    area = [[0, 0], [432, 468]]
    if not(area[0][0] <= dados[0] <= area[1][0]):
        return "fora"
    
    if not(area[0][1] <= dados[1] <= area[1][1]):
        return "fora"
    
    return "dentro"

print(juiz(list(map(int, input().split()))))