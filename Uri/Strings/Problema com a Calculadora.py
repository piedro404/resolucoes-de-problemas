def calculadoraTxt(texto: str):
    sum = 0
    digs = "0"
    
    for x in texto:
        if x.isdigit():
            digs += x
        
        else:
            if digs:
                sum += int(digs)
                digs = "0"
                
    sum += int(digs)
    
    return sum
                
for _ in range(int(input())):
    print(calculadoraTxt(str(input())))