def fliper(dados):
    if dados[0] == 1:
        if dados[1] == 1:
            return "A"

        return "B"
    
    return "C"

print(fliper(list(map(int, input().split()))))