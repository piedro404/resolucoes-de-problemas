def telefone_sem_fio(frase, resps):
    placar = [0, 0]
    desempate = [True, True]
    for x in range(len(frase)):
        if frase[x] == resps[0][x]:
            placar[0] += 1
        if frase[x] == resps[1][x]:
            placar[1] += 1
        if desempate[0] == desempate[1]:
            if placar[0] > placar[1]:
                desempate[1] = False
            elif placar[0] < placar[1]:
                desempate[0] = False
            
    
    if placar[0] == placar[1]:
        if desempate[0] == desempate[1]:
            return "empate"
        
        if desempate[0]:
            return "time 1"
        
        return "time 2"
    
    if placar[0] > placar[1]:
        return "time 1"
        
    return "time 2"
    
for x in range(int(input())):
    resps = []
    frase = str(input())
    for _ in range(2):
        resps.append(str(input()))
        
    print(f"Instancia {x+1}")
    print(telefone_sem_fio(frase, resps))
    print()