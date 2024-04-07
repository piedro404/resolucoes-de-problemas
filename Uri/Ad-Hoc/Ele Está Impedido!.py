def impedido(atacante, defensores):
    defensores_atacante = 0
    
    for defe in defensores:
        if defe <= atacante:
            defensores_atacante += 1
    
    if defensores_atacante > 1:
        return "N"
    
    return "Y"

while True:
    try:
        dados = list(map(int, input().split()))
        if dados[0] == dados[1] == 0:
            break
        
        atacante = min(list(map(int, input().split())))
        defensores = list(map(int, input().split()))
        print(impedido(atacante, defensores))

    except EOFError:
        break
    