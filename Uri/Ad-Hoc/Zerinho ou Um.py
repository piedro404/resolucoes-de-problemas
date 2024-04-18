def letra(dados):
    if dados[0] == dados[1] == dados[2]:
        return "*"

    if dados[0] in [0, 1] and dados[1] == dados[2]:
        return "A"
    
    if dados[1] in [0, 1] and dados[0] == dados[2]:
        return "B"
    
    return "C"

while True:
    try:
        print(letra(list(map(int, input().split()))))
    except EOFError:
        break