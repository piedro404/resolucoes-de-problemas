def Number(texto):
    if len(texto) == 5:
        return 3
    
    else:
        if (texto[0] == "o" and texto[1] == "n") or (texto[0] == "o" and texto[2] == "e") or (texto[1] == "n" and texto[2] == "e"):
            return 1
        
        else:
            return 2
        
for _ in range(int(input())):
    print(Number(str(input())))
            