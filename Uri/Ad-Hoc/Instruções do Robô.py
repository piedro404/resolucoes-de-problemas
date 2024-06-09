def ordem(listaOrdem: list, p: int, dados: list):
    if dados[0] == "LEFT": 
        p-=1
        listaOrdem.append(dados[0])
    elif dados[0] == "RIGHT":
        p+=1
        listaOrdem.append(dados[0])
    else:
        p, listaOrdem = ordem(listaOrdem, p, listaOrdem[int(dados[2])-1].split())
    
    return p, listaOrdem

for _ in range(int(input())):
    listaOrdem = []
    p = 0
    for _ in range(int(input())):
        dados = input().split()
        
        p, listaOrdem = ordem(listaOrdem, p, dados)
    
    print(p)
        
        