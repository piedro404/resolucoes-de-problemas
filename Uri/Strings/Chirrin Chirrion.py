def retorno(dados):
    new_dados = []
    for dado in dados:
        if dado[1] == "chirrin":
            new_dados.append(dado[0])
            
        elif dado[1] == "chirrion":
            if dado[0] in new_dados:
                new_dados.remove(dado[0])
    new_dados.sort()            
    
    return new_dados

def printList(list):
    print("TOTAL")
    for x in list:
        print(x)

for _ in range(int(input())):
    dados = []     
    for _ in range(int(input())):
        dados.append(list(input().split()))    
    
    printList(retorno(dados))