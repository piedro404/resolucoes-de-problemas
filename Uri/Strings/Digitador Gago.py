def gago(texto):
    new_texto = []
    
    for x in texto:
        if len(x) >= 5:
            if x[0:1] == x[2:3]:
                x = x[2::]
                
        new_texto.append(x)
    
    return " ".join(new_texto)

print(gago(input().split()))